# Generated from fog-proxmox-0.5.1.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-proxmox

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.6.0
Release: 1%{?dist}
Summary: Module for the 'Fog' gem to support Proxmox VE
Group: Development/Languages
License: GPLv3
URL: https://github.com/fog/fog-proxmox
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.3
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(fog-core) >= 1.45
Requires: %{?scl_prefix}rubygem(fog-core) < 2
Requires: %{?scl_prefix}rubygem(fog-json) >= 1.0
Requires: %{?scl_prefix}rubygem(fog-json) < 2
Requires: %{?scl_prefix}rubygem(ipaddress) >= 0.8
Requires: %{?scl_prefix}rubygem(ipaddress) < 1
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.3
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end generated dependencies

%description
This library can be used as a module for `fog`.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/console
%{_bindir}/setup
%{gem_instdir}/.bundle
%{gem_instdir}/.codeclimate.yml
%{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%{gem_instdir}/.gitlab-ci.yml
%exclude %{gem_instdir}/.rubocop.yml
%{gem_instdir}/.ruby-gemset
%{gem_instdir}/.solargraph.yml
%exclude %{gem_instdir}/.travis.yml
%{gem_instdir}/.vscode
%{gem_instdir}/CODE_OF_CONDUCT.md
%{gem_instdir}/ISSUE_TEMPLATE.md
%license %{gem_instdir}/LICENSE
%{gem_instdir}/SUPPORT.md
%{gem_instdir}/bin
%{gem_instdir}/fogproxmox.png
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docs
%{gem_instdir}/examples
%{gem_instdir}/fog-proxmox.gemspec
%{gem_instdir}/spec

%changelog
* Tue Apr 16 2019 Tristan Robert <tristan.robert.44@gmail.com> 0.6.0-1
- Update to 0.6.0

* Thu Jan 03 2019 Tristan Robert <tristan.robert.44@gmail.com> 0.5.5-1
- Update to 0.5.5

* Wed Nov 14 2018 Tristan Robert <tristan.robert.44@gmail.com> 0.5.3-1
- Update to 0.5.3

* Fri Oct 05 2018 Tristan Robert <tristan.robert.44@gmail.com> 0.5.2-1
- Update to 0.5.2

* Thu Sep 13 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.5.1-1
- Add rubygem-fog-proxmox generated by gem2rpm using the scl template

