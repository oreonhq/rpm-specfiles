%global source0_hash 19fa898133c2c26cdbb5d09f6998c1e137ad9427a046663e55adfe18b950d894

%global gem_name formatador

%{!?_with_bootstrap: %global bootstrap 0}

Name: rubygem-%{gem_name}
Version: 1.2.3
Release: 2%{?dist}
Summary: Ruby STDOUT text formatting
License: MIT
URL: https://github.com/geemus/formatador
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
%if ! 0%{?bootstrap}
# The `reline` dependency was introduced here:
# https://github.com/geemus/formatador/pull/60
# and it is explicitly stated here, because `reline` is about to be removed
# from StdLib according to:
# https://github.com/janlelis/unicode-display_width/issues/31#issuecomment-3188132741
BuildRequires: rubygem(reline)
BuildRequires: rubygem(shindo)
%endif
BuildArch: noarch

%description
STDOUT text formatting.

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
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
%if ! 0%{?bootstrap}
pushd .%{gem_instdir}
# if we don't use -Ilib, the already installed (perhaps older) gem will be used
# but we want to test the actually packaged
RUBYOPT=-Ilib shindo
popd
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/changelog.txt
%{gem_instdir}/formatador.gemspec
%{gem_instdir}/tests

%changelog
%autochangelog
