%global source0_hash 72b847b5cc961589dde2c395af0108c86ff0119f42d4648d25b5440ebb10059e

%global gem_name launchy

Name: rubygem-%{gem_name}
Version: 3.1.1
Release: 1%{?dist}
Summary: Helper class for cross-platform launching of applications
License: ISC
URL: http://github.com/copiousfreetime/launchy
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/copiousfreetime/launchy/pull/132
# https://github.com/copiousfreetime/launchy/commit/b7cef9d7ca05258972b5b267a07254ce648d7f82
# Fix compatibility with newer minitest
Patch0:  %{gem_name}-pr132-newer-minitest.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest) >= 5.0
BuildRequires: rubygem(addressable)
BuildArch: noarch

%description
Launchy is helper class for launching cross-platform applications in a fire
and forget manner. There are application concepts (browser, email client, etc)
that are common across all platforms, and they may be launched differently on
each platform. Launchy is here to make a common approach to launching external
application from within ruby programs.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd ./%{gem_instdir}
%patch -P0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# Disable code coverage.
sed -i '/[cC]ov/ s/^/#/' spec/spec_helper.rb

# It does not look like the test suite is designed to pass anywhere else than
# on authors computer :/ Skip the failing tests ...
sed -i '/prints the command on stdout when using --dry-run/ a \   skip' spec/cli_spec.rb
sed -i '/asssumes we open a local file if we have an exception if we have an invalid scheme and a valid path/ a \    skip' spec/launchy_spec.rb
sed -i '/when host_os is ...host_os.. the appropriate .app_list. method is called/ a \      skip' spec/applications/browser_spec.rb
sed -i '/the BROWSER environment variable overrides any host defaults on/ a \      skip' spec/applications/browser_spec.rb

ruby -Ilib:spec -e 'Dir.glob "./spec/**/*_spec.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/launchy
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/HISTORY.md
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%{gem_instdir}/tasks

%changelog
%autochangelog
