%global source0_hash 42f52ce12c6fe079bac8a804c66522a0eefe176b845a62df829defe0e37214a4
%global gem_name launchy
Name: rubygem-%{gem_name}
Version: 2.4.3
Release:        1%{?dist}
Summary:        Helper class for cross-platform launching of applications
License: ISC
URL: http://github.com/copiousfreetime/launchy
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:  %{gem_name}-pr132-newer-minitest.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(addressable)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i '/[cC]ov/ s/^/#/' spec/spec_helper.rb
sed -i '/prints the command on stdout when using --dry-run/ a \   skip' spec/cli_spec.rb
sed -i '/asssumes we open a local file if we have an exception if we have an invalid scheme and a valid path/ a \    skip' spec/launchy_spec.rb
sed -i '/when host_os is ...host_os.. the appropriate .app_list. method is called/ a \      skip' spec/applications/browser_spec.rb
sed -i '/the BROWSER environment variable overrides any host defaults on/ a \      skip' spec/applications/browser_spec.rb
ruby -Ilib:spec -e 'Dir.glob "./spec/**/*_spec.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-launchy-doc -f %{oreon_filedir}/rubygem-launchy-doc.list

%changelog

%autochangelog
