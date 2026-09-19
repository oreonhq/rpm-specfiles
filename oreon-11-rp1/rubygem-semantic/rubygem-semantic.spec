%global source0_hash 3cdbb48f59198ebb782a3fdfb87b559e0822a311610db153bae22777a7d0c163

%global gem_name semantic

Name:           rubygem-%{gem_name}
Version:        1.6.1
Release:        18%{?dist}
Summary:        Utility class for parsing, storing, and comparing versions

License:        MIT
URL:            https://rubygems.org/gems/%{gem_name}
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildArch:      noarch

BuildRequires:  rubygems-devel
BuildRequires:  rubygem(rspec)

%description
Semantic Version utility class for parsing, storing, and comparing versions.

%package doc
Summary:        Documentation for %{name}
Requires:       rubygems

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -r %{buildroot}%{gem_instdir}/spec

%check
rspec -Ilib spec

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
%autochangelog
