%global source0_hash 248193992ef1730a0c9ec579999ef2256a2b3a32a9bd9d708a1e12544a489ec2

%global gem_name safe_yaml
# Although there are tests
# the dependancies aren't in Fedora yet
%global enable_tests 0

Summary:       Parse YAML safely
Name:          rubygem-%{gem_name}
Version:       1.0.4
Release:       23%{?dist}
License:       MIT
URL:           http://dtao.github.com/safe_yaml/
Source0:       https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix Ruby 2.5 compatibility.
# https://github.com/dtao/safe_yaml/pull/90
Patch0:        rubygem-safe_yaml-1.0.4-Fix-uninitialized-constant-DateTime.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
%if 0%{?enable_tests}
BuildRequires: rubygem(hashie)
#BuildRequires: rubygem(heredoc_unindent)
#BuildRequires: rubygem(ostruct)
BuildRequires: rubygem(rspec)
#BuildRequires: rubygem(yaml)
%endif
BuildArch:     noarch

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

# Remove build leftovers.
rm -rf %{buildroot}%{gem_instdir}/{.rvmrc,.document,.require_paths,.gitignore,.travis.yml,.rspec,.gemtest,.yard*}
rm -rf %{buildroot}%{gem_instdir}/%{gem_name}.gemspec
rm -rf %{buildroot}%{gem_instdir}/bundle_install_all_ruby_versions.sh

%if 0%{?enable_tests}
%check
pushd .%{gem_instdir}
rspec -Ilib spec
popd
%endif

%files
%{_bindir}/safe_yaml
%doc %{gem_instdir}/LICENSE.txt
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/CHANGES.md
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/run_specs_all_ruby_versions.sh
%{gem_instdir}/spec

%changelog
%autochangelog
