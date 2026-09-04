%global source0_hash 89e186d2aeb8b8237b2ad8ed04bf47907b7acd475afff290d3f271b5f84c4d24

%global gem_name pathspec

Name:           rubygem-%{gem_name}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Use to match path patterns such as gitignore

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://rubygems.org/gems/%{gem_name}
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildArch:      noarch

BuildRequires:  rubygems-devel
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(fakefs)

%description
Use to match path patterns such as gitignore.

%package doc
Summary:        Documentation for %{name}
Requires:       rubygems

%description doc
Documentaion for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
chmod 0755 %{buildroot}%{gem_instdir}/bin/pathspec-rb
mv %{buildroot}%{gem_instdir}/bin/pathspec-rb %{buildroot}%{_bindir}

%check
echo > spec/spec_helper.rb
rspec -Ilib spec

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_libdir}
%{gem_spec}
%{_bindir}/pathspec-rb
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec

%changelog
%autochangelog
