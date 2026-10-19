%global source0_hash 248193992ef1730a0c9ec579999ef2256a2b3a32a9bd9d708a1e12544a489ec2
%global gem_name safe_yaml
%global enable_tests 0
Summary:        Parse YAML safely
Name:          rubygem-%{gem_name}
Version:       1.0.4
Release:        23%{?dist}
License:       MIT
URL:           http://dtao.github.com/safe_yaml/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:        rubygem-safe_yaml-1.0.4-Fix-uninitialized-constant-DateTime.patch
%if 0%{?enable_tests}
%endif
BuildArch:     noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
The SafeYAML gem provides an alternative implementation of 
YAML.load suitable for accepting user input in Ruby applications. 
Unlike Ruby's built-in implementation of YAML.load, SafeYAML's 
version will not expose apps to arbitrary code execution exploits.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%patch -P0 -p1

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
rm -rf %{buildroot}%{gem_instdir}/{.rvmrc,.document,.require_paths,.gitignore,.travis.yml,.rspec,.gemtest,.yard*}
rm -rf %{buildroot}%{gem_instdir}/%{gem_name}.gemspec
rm -rf %{buildroot}%{gem_instdir}/bundle_install_all_ruby_versions.sh
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if 0%{?enable_tests}
%check

pushd .%{gem_instdir}
rspec -Ilib spec
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-safe_yaml-doc -f %{oreon_filedir}/rubygem-safe_yaml-doc.list

%changelog

%autochangelog
