%global source0_hash 284aae4adc431498a8f2a8e6027da72bca5f2ea8134d770ffc6f8e45bf6b29f9

# Generated from nio4r-1.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name nio4r

%global libev_version 4.33

Name: rubygem-%{gem_name}
Version: 2.6.1
Release: 10%{?dist}
Summary: New IO for Ruby
# The entire source code is MIT, bundled libev is BSD-2-Clause OR GPL-2.0-or-later
License: MIT AND (BSD-2-Clause OR GPL-2.0-or-later)
URL: https://github.com/socketry/nio4r
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/socketry/nio4r/pull/328
# ruby3.5.0dev removes SSLContext#set_minmax_proto_version
Patch0:  %{gem_name}-pr328-support-rubu35-openssl.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: rubygem(rspec)
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc

# As bundled libev ev.c is modified from original one,
# we have to use the bundled libev instead of separating it and
# using system libev.
# See below commits.
# Release the GIL when libev polls
# https://github.com/socketry/nio4r/commit/6801433
# A more productive message re: GVL
# https://github.com/socketry/nio4r/commit/fba5c68
Provides: bundled(libev) = %{libev_version}

%description
Cross-platform asynchronous I/O primitives for scalable network clients and
servers. Inspired by the Java NIO API, but simplified for ease-of-use.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
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
pushd .%{gem_instdir}
# Check libev version correctness.
EV_VERSION_MAJOR=$(grep EV_VERSION_MAJOR ext/libev/ev.h | cut -d ' ' -f3)
EV_VERSION_MINOR=$(grep EV_VERSION_MINOR ext/libev/ev.h | cut -d ' ' -f3)
[ "${EV_VERSION_MAJOR}.${EV_VERSION_MINOR}" = '%{libev_version}' ]

rspec -I$(dirs +1)%{gem_extdir_mri} spec

# Test also pure Ruby implementation.
NIO4R_PURE=true rspec -I$(dirs +1)%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/license.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/logo.png
%{gem_instdir}/rakelib
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/changes.md
%{gem_instdir}/examples
%{gem_instdir}/nio4r.gemspec
%doc %{gem_instdir}/readme.md
%{gem_instdir}/spec

%changelog
%autochangelog
