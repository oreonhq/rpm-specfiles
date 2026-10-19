%global source1_hash 64343da0ae4cf41a3ba8c44bd6ffe186a4f93d8d72314a751d5fb245237805d3
%global source0_hash f246bb1152159098f5d5619b92e373c73db77769bf3e0c4b6336feeb934bc8d2
%global gem_name bootsnap
Name: rubygem-%{gem_name}
Version: 1.15.0
Release:        1%{?dist}
Summary:        Boot large ruby/rails apps faster
License: MIT
URL: https://github.com/Shopify/bootsnap
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/Shopify/bootsnap/archive/refs/tags/v1.15.0.tar.gz
Patch0: rubygem-bootsnap-1.15.0-Use-RbConfig-CONFIG-rubylibdir-to-check-for-stdlib-files.patch
Patch1: rubygem-bootsnap-1.15.0-Use-RbConfig-CONFIG-rubylibdir-to-check-for-stdlib-files-test.patch
Patch2: rubygem-bootsnap-1.16.0-Fix-compatibility-with-Minitest-5.19.patch
Patch3: rubygem-bootsnap-pr460-KernelRequireTest-method-invocation-check.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(bundler)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(msgpack)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Bootsnap is a library that plugs into Ruby, with optional support
for ActiveSupport and YAML, to optimize and cache expensive computations.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%patch 0 -p1

pushd %{_builddir}
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
popd

sed -i -e "/^\s*\$CFLAGS / s/^/#/g" \
  ext/bootsnap/extconf.rb

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name}/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}
rm -rf %{buildroot}%{gem_instdir}/ext/
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/test test
cat <<GEMFILE > Gemfile
gem "minitest"
gem "mocha"
gem "msgpack"
GEMFILE
RUBYOPT="-I$(dirs +1)%{gem_extdir_mri}:$(dirs +1)%{gem_libdir}" \
  ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-bootsnap-doc -f %{oreon_filedir}/rubygem-bootsnap-doc.list

%changelog

%autochangelog
