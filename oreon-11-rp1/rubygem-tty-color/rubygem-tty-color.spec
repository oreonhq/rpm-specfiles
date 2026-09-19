%global source0_hash 6f9c37ca3a4e2367fb2e6d09722762647d6f455c111f05b59f35730eeb24332a

# Generated from tty-color-0.6.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name tty-color

Name: rubygem-%{gem_name}
Version: 0.6.0
Release: 11%{?dist}
Summary: Terminal color capabilities detection
License: MIT
URL: https://ttytoolkit.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygem(rspec) >= 3.0
BuildArch: noarch

%description
Terminal color capabilities detection.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
