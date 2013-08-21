%define gem_name daemon_controller

%if 0%{?fedora} >= 19
%global gem_extdir %{gem_extdir_mri}
%endif

%if 0%{?rhel} >= 5
%global rubyabi 1.8
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname daemon_controller
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}
%endif

Summary: A library for implementing daemon management capabilities
Name: rubygem-%{gemname}
Version: 1.1.5
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/FooBarWidget/daemon_controller/tree/master
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem

%if 0%{?fedora} >= 19
Requires:      ruby(release)
%else
Requires:      ruby(abi) >= %{rubyabi}
BuildRequires: ruby(abi) >= %{rubyabi}
%endif

Requires: rubygems
BuildRequires: ruby rubygems rubygem-rspec
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A library for robust daemon management.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep

%build

%install
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%check
pushd %{buildroot}%{geminstdir}
# be explicit so localhost doesn't resolve to an ipv6 address.
%{__sed} -i 's/localhost/127.0.0.1/g' spec/daemon_controller_spec.rb
RUBYOPT="I%{buildroot}%{geminstdir}/lib Ispec" spec spec/

%files
%defattr(-, root, root, -)
%dir %{geminstdir}
%{geminstdir}/lib
%doc %{geminstdir}/LICENSE.txt
%doc %{geminstdir}/README.markdown
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(-, root, root, -)
%{geminstdir}/*.gemspec
%{gemdir}/doc/%{gemname}-%{version}
%{geminstdir}/spec
%{geminstdir}/debian.template

%changelog
* Wed Aug 21 2013 Brett Lentz <blentz@redhat.com> - 1.1.5-1
- Update to 1.1.5

 Mon Apr 25 2011  Peng Wu <pwu@redhat.com> - 0.2.6-1
- Update to version 0.2.6

* Thu Apr 21 2011  Peng Wu <pwu@redhat.com> - 0.2.5-3
- Run test suite

* Wed Apr 20 2011  Peng Wu <pwu@redhat.com> - 0.2.5-2
- Fixes the spec

* Wed Apr 20 2011 Peng Wu <pwu@redhat.com> - 0.2.5-1
- Initial eackage
