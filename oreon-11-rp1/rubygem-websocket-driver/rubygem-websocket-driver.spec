%global source0_hash a280c3f44dcbb0323d58bc78dc49350c05d589ab7d13267fcff08d9d5ae76b28

# Generated from websocket-driver-0.3.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name websocket-driver

Name: rubygem-%{gem_name}
Version: 0.7.5
Release: 18%{?dist}
Summary: WebSocket protocol handler with pluggable I/O
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: http://github.com/faye/websocket-driver-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone --no-checkout https://github.com/faye/websocket-driver-ruby.git
# cd websocket-driver-ruby && git archive -v -o websocket-driver-ruby-0.7.5-tests.txz 0.7.5 spec/
Source1: websocket-driver-ruby-%{version}-tests.txz
# Use port 80 explicitly in tests
# https://github.com/faye/websocket-driver-ruby/pull/88
Patch0: rubygem-websocket-driver-0.7.5-Use-port-80-explicitly-in-tests.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
BuildRequires: rubygem(base64)
BuildRequires: rubygem(websocket-extensions)
BuildRequires: rubygem(rspec)

%description
This module provides a complete implementation of the WebSocket protocols that
can be hooked up to any TCP library. It aims to simplify things by decoupling
the protocol details from the I/O layer, such that users only need to implement
code to stream data in and out of it without needing to know anything about how
the protocol actually works. Think of it as a complete WebSocket system with
pluggable I/O.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

%build
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
pushd .%{gem_instdir}

# Copy tests into place (patch does not work with symlinks)
cp -r %{_builddir}/spec .

cat %{PATCH0} | patch -p1

# Bundler
sed -i '/bundler/ s/^/#/' spec/spec_helper.rb

rspec -I$(dirs +1)%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
