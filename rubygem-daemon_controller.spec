# Generated from daemon_controller-0.2.5.gem by gem2rpm -*- rpm-spec -*-
%global rubyabi 1.8
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname daemon_controller
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A library for implementing daemon management capabilities
Name: rubygem-%{gemname}
Version: 0.2.5
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/FooBarWidget/daemon_controller/tree/master
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: rubygems
BuildRequires: ruby rubygems rubygem-rspec
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

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

%changelog
* Thu Apr 21 2011  Peng Wu <pwu@redhat.com> - 0.2.5-3
- Run test suite

* Wed Apr 20 2011  Peng Wu <pwu@redhat.com> - 0.2.5-2
- Fixes the spec

* Wed Apr 20 2011 Peng Wu <pwu@redhat.com> - 0.2.5-1
- Initial package
