# Generated from daemon_controller-0.2.5.gem by gem2rpm -*- rpm-spec -*-
%global rubyabi 1.9.1
%define gem_name daemon_controller

Summary: A library for implementing daemon management capabilities
Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/FooBarWidget/daemon_controller/tree/master
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
BuildRequires: ruby rubygems-devel rubygem(rspec-core)
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
mkdir -p %{buildroot}%{gem_dir}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}

%check
pushd %{buildroot}%{gem_instdir}
# be explicit so localhost doesn't resolve to an ipv6 address.
%{__sed} -i 's/localhost/127.0.0.1/g' spec/daemon_controller_spec.rb
rspec -I%{buildroot}%{gem_libdir} -Ispec spec/
popd

%files
%defattr(-, root, root, -)
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.markdown
%{gem_cache}
%{gem_spec}

%files doc
%defattr(-, root, root, -)
%{gem_instdir}/*.gemspec
%{gem_docdir}
%{gem_instdir}/spec

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 13 2012 Brett Lentz <blentz@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 06 2012 Vít Ondruch <vondruch@redhat.com> - 0.2.6-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Apr 25 2011  Peng Wu <pwu@redhat.com> - 0.2.6-1
- Update to version 0.2.6

* Thu Apr 21 2011  Peng Wu <pwu@redhat.com> - 0.2.5-3
- Run test suite

* Wed Apr 20 2011  Peng Wu <pwu@redhat.com> - 0.2.5-2
- Fixes the spec

* Wed Apr 20 2011 Peng Wu <pwu@redhat.com> - 0.2.5-1
- Initial package
