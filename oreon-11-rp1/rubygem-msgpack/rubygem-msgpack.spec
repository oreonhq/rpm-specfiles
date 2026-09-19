%global source0_hash 59ab62fd8a4d0dfbde45009f87eb6f158ab2628a7c48886b0256f175166baaa8

# Generated from msgpack-0.5.9.gem by gem2rpm -*- rpm-spec -*-
%global gem_name msgpack

Name: rubygem-%{gem_name}
Version: 1.7.2
Release: 7%{?dist}
Summary: MessagePack, a binary-based efficient data interchange format
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: http://msgpack.org/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# The msgpack gem doesn't ship with the test suite.
# You may check it out like so:
# git clone --no-checkout https://github.com/msgpack/msgpack-ruby
# git -C msgpack-ruby archive -v -o msgpack-1.7.2-spec.txz v1.7.2 spec/
Source1: %{gem_name}-%{version}-spec.txz
# https://github.com/msgpack/msgpack-ruby/commit/0737d2e8edbda1520d97ef1851efa4c2d57b469b
# support ruby3.4 formatting change
Patch0:  msgpack-1.7.2-ruby34-format.patch

BuildRequires: gcc
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires:  rubygem(rspec)
# BuildRequires: rubygem(rake-compiler) < 0.9
# BuildRequires: rubygem(json) < 2
# BuildRequires: rubygem(yard) < 0.9

%description
MessagePack is a binary-based efficient object serialization library. It
enables to exchange structured objects between many languages like JSON. But
unlike JSON, it is very fast and small.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
(
cd %{builddir}/spec
%patch -P0 -p2
)

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -ar .%{gem_extdir_mri}/{gem.build_complete,%{gem_name}} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

# Disable the test suite for ppc64le
# https://github.com/msgpack/msgpack-ruby/issues/265
%ifnarch ppc64le
%check
pushd .%{gem_instdir}
ln -s %{builddir}/spec spec
rm -rf spec/jruby
rspec -Ilib -I%{buildroot}%{gem_extdir_mri} spec
popd
%endif

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/README.md
%{gem_instdir}/msgpack.gemspec

%changelog
%autochangelog
