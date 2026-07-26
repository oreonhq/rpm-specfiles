%global source0_hash f246bb1152159098f5d5619b92e373c73db77769bf3e0c4b6336feeb934bc8d2

# Generated from bootsnap-1.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bootsnap

Name: rubygem-%{gem_name}
Version: 1.15.0
Release: 14%{?dist}
Summary: Boot large ruby/rails apps faster
License: MIT
URL: https://github.com/Shopify/bootsnap
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# The bootsnap gem doesn't ship with the test suite.
# You may check it out like so:
# git clone http://github.com/Shopify/bootsnap.git --no-checkout
# cd bootsnap && git archive -v -o bootsnap-1.15.0-tests.txz v1.15.0 test/
Source1: %{gem_name}-%{version}-tests.txz
# Correctly determine StdLib files as stable.
# https://github.com/Shopify/bootsnap/issues/431
# https://github.com/Shopify/bootsnap/commit/72202aab5e5b3602ece4e8748bcdeefe2d789ab5
Patch0: rubygem-bootsnap-1.15.0-Use-RbConfig-CONFIG-rubylibdir-to-check-for-stdlib-files.patch
Patch1: rubygem-bootsnap-1.15.0-Use-RbConfig-CONFIG-rubylibdir-to-check-for-stdlib-files-test.patch
# Minitest 5.19 puts `MiniTest` constant behind environment variable.
# https://github.com/Shopify/bootsnap/pull/452
Patch2: rubygem-bootsnap-1.16.0-Fix-compatibility-with-Minitest-5.19.patch
# Patch for ruby3.3.0dev: relax method invocation checking for KernelRequireTest
# https://github.com/Shopify/bootsnap/pull/460
Patch3: rubygem-bootsnap-pr460-KernelRequireTest-method-invocation-check.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel >= 2.0.0
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(msgpack)
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc

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

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test test

cat <<GEMFILE > Gemfile
gem "minitest"
gem "mocha"
gem "msgpack"
GEMFILE

# Plese note that `KernelTest` testcases are executed in separate process,
# which needs to subsequetnly load `bootsnap/setup`, therefore we need to
# use RUBYOPT to define load paths. This is normally handled by Bunler and
# `gemspec` directive. But we would need to have the bootsnap .gemspec in
# the directory.
RUBYOPT="-I$(dirs +1)%{gem_extdir_mri}:$(dirs +1)%{gem_libdir}" \
  ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/bootsnap
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/exe
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
