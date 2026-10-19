%global source1_hash c77658a2d70b38855c5c6c44b787896b39307104d30c434a37d122b329d3a6f0
%global source0_hash 51630e43425078311c056ca75f961bb3bda1641ab36e44ad4c455e0b0e4a231c
%global gem_name ffi
Name: rubygem-%{gem_name}
Version: 1.17.0
Release:        1%{?dist}
Summary:        FFI Extensions for Ruby
License: BSD-3-Clause
URL: https://github.com/ffi/ffi/wiki
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/ffi/ffi/archive/refs/tags/v1.17.0.tar.gz
Patch0: rubygem-ffi-1.17.0-Ensure-GC-ing-closures-before-fork.patch
Patch1: rubygem-ffi-pr1146-make-ffi_function-sharable.patch
Patch2: rubygem-ffi-pr1152-Ractor_take-deprecation.patch
Patch3: rubygem-ffi-350b3a1-fix-ractor-tests.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libffi-devel
BuildRequires:  make
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(bigdecimal)
BuildRequires:  rubygem(fiddle)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby-FFI is a ruby extension for programmatically loading dynamic
libraries, binding functions within them, and calling those functions
from Ruby code. Moreover, a Ruby-FFI extension works without changes
on Ruby and JRuby. Discover why should you write your next extension
using Ruby-FFI here[http://wiki.github.com/ffi/ffi/why-use-ffi].

%package doc
Summary: Documentation for %{name}
License: BSD-3-Clause AND MIT
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n  %{gem_name}-%{version} -a 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{gem_instdir}/ext/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

ln -s $(pwd)/spec .%{gem_instdir}/spec
pushd .%{gem_instdir}
pushd spec/ffi/fixtures
make JFLAGS="%{optflags}"
popd
RUBYOPT="-I$(dirs +1)%{gem_extdir_mri}" rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-ffi-doc -f %{oreon_filedir}/rubygem-ffi-doc.list

%changelog

%autochangelog
