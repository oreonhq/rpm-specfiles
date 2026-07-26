%global source0_hash 36f181e956762ae970da9129683967e6e6abe26fa1b2e120a9139776627b0206

# tests won't work until dependent packages are available
%bcond_without tests

%global app_root %{_datadir}/%{name}
%global gem_name sugarjar
%global version 2.0.2

%global common_description %{expand:
Sugarjar is a utility to help making working with git
and GitHub easier. In particular it has a lot of features
to make rebase-based and squash-based workflows simpler.}

Name: rubygem-%{gem_name}
Version: %{version}
Release: 2%{?dist}
Summary: A git/GitHub helper utility
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: http://www.github.com/jaymzh/sugarjar
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem
# git clone https://github.com/jaymzh/sugarjar.git
# version='1.1.0'
# git checkout v${version?}
# tar -cf ../rubygem-sugarjar/rubygem-sugarjar-${version?}-specs.tar spec/
Source1: %{name}-%{version}-specs.tar
BuildRequires: rubygems-devel
%if %{with tests}
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(deep_merge)
BuildRequires: rubygem(mixlib-log)
BuildRequires: rubygem(mixlib-shellout)
BuildRequires: gh
BuildRequires: git
%endif
BuildArch: noarch

%description
%{common_description}

%package -n sugarjar
Summary: A git/github helper utility
Requires: ruby(release) >= 3.2
Requires: gh
Requires: git
Requires: git-core
Requires: rubygem(deep_merge)
Requires: rubygem(mixlib-log)
Requires: rubygem(mixlib-shellout)
Requires: rubygem(pastel)
%description -n sugarjar
%{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{bash_completions_dir}
cp -a %{buildroot}%{gem_instdir}/extras/sugarjar_completion.bash %{buildroot}%{bash_completions_dir}/sugarjar_completion.bash

mkdir -p %{buildroot}%{_docdir}/sugarjar/examples
cp -a %{buildroot}/%{gem_instdir}/examples/* %{buildroot}%{_docdir}/sugarjar/examples/
cp -a %{buildroot}/%{gem_instdir}/{README.md,LICENSE,CONTRIBUTING.md,CHANGELOG.md} %{buildroot}%{_docdir}/sugarjar/

%if %{with tests}
%check
pushd .%{gem_instdir}
cp -a %{_builddir}/spec .
# These two specs require a git repo, so we exclude them. Filed a bug
# upstream: https://github.com/jaymzh/sugarjar/issues/194
rm spec/repoconfig_spec.rb
rm spec/commands/feature_spec.rb
rspec spec
%endif

%clean
rm -rf %{buildroot}

%files -n sugarjar
%dir %{gem_instdir}
%{_bindir}/sj
%{gem_instdir}/bin
%dir %{bash_completions_dir}
%{bash_completions_dir}/sugarjar_completion.bash
%license %{gem_instdir}/LICENSE
%doc %{_docdir}/sugarjar/{README.md,LICENSE,CONTRIBUTING.md,CHANGELOG.md}
%doc %{_docdir}/sugarjar/examples/*
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/{Gemfile,sugarjar.gemspec,CHANGELOG.md,README.md,LICENSE,CONTRIBUTING.md}
%exclude %{gem_instdir}/extras
%exclude %{gem_instdir}/examples
# We don't have ri/rdoc in our sources
%exclude %{gem_docdir}
%{gem_spec}

%changelog
%autochangelog
