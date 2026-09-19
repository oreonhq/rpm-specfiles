%global source0_hash e0b3a627cd53d430525b69d57e06facd2fbeaa304b7e425582e39570f84ffb3d

%global gem_name ffi

Name: rubygem-%{gem_name}
Version: 1.17.0
Release: 7%{?dist}
Summary: FFI Extensions for Ruby
License: BSD-3-Clause
URL: https://github.com/ffi/ffi/wiki
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/ffi/ffi.git --no-checkout
# cd ffi && git archive -v -o ffi-1.17.0-spec.txz v1.17.0 spec/
Source1: %{gem_name}-%{version}-spec.txz
# Fix test suite `Aborted (core dumped)` on ppc64le/s390x
# https://bugzilla.redhat.com/show_bug.cgi?id=2313598
# https://github.com/ffi/ffi/pull/1124
Patch0: rubygem-ffi-1.17.0-Ensure-GC-ing-closures-before-fork.patch
# Fix making FFI::Function shareable for Ractor
# https://github.com/ffi/ffi/pull/1146
Patch1: rubygem-ffi-pr1146-make-ffi_function-sharable.patch
# Use Ractor#value instead of deprecated #take
# https://github.com/ffi/ffi/pull/1152
Patch2: rubygem-ffi-pr1152-Ractor_take-deprecation.patch
# Fix Ractor tests on FFI::DynamicLibrary
# https://github.com/ffi/ffi/commit/350b3a1327396839b6c78d335fc9c6197737598b
Patch3: rubygem-ffi-350b3a1-fix-ractor-tests.patch
BuildRequires: make
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
BuildRequires: libffi-devel
BuildRequires: rubygem(rspec) >= 3
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(fiddle)

%description
Ruby-FFI is a ruby extension for programmatically loading dynamic
libraries, binding functions within them, and calling those functions
from Ruby code. Moreover, a Ruby-FFI extension works without changes
on Ruby and JRuby. Discover why should you write your next extension
using Ruby-FFI here[http://wiki.github.com/ffi/ffi/why-use-ffi].

%package doc
Summary: Documentation for %{name}
# The spec/ are MIT licensed.
License: BSD-3-Clause AND MIT
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version} -a 1

%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
ln -s $(pwd)/spec .%{gem_instdir}/spec

pushd .%{gem_instdir}
# Build the test library with Fedora build options.
pushd spec/ffi/fixtures
make JFLAGS="%{optflags}"
popd

RUBYOPT="-I$(dirs +1)%{gem_extdir_mri}" rspec spec
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/COPYING
%license %{gem_instdir}/LICENSE
%license %{gem_instdir}/LICENSE.SPECS
%{gem_libdir}
%{gem_instdir}/sig
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/samples
%{gem_instdir}/ffi.gemspec
%{gem_instdir}/rakelib

%changelog
%autochangelog
