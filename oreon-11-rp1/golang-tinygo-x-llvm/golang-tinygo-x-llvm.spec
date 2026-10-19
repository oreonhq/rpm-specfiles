%global source0_hash c1a7fce4ce2a2c36caaeb4f7ca386da58cfc61a1a946460dc9855ef3b43d6b64
%bcond check 0
%global debug_package %{nil}
%global min_llvm 14
%global max_llvm 19
%global goipath         tinygo.org/x/go-llvm
%global forgeurl        https://github.com/tinygo-org/go-llvm
%global commit          b8f170971e747fec20a03b25a4490f627140709a
%gometa -L -f
%global common_description %{expand:
This library provides bindings to a system-installed LLVM.}
%global golicenses      LICENSE.txt
%global godocs          README.markdown
Name:           golang-tinygo-x-llvm
Version:        0
Release:        1%{?dist}
Summary:        Go bindings to a system-installed LLVM
License:        Apache-2.0 AND NCSA
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/go-llvm-%{commit}.tar.gz
%{lua:
local llvm_supported_versions = 'llvm_supported_versions'
for version=tonumber(rpm.expand('%min_llvm')),tonumber(rpm.expand('%max_llvm')) do
  if version ~= 16 then -- LLVM16 is no longer supported
    print('BuildRequires: llvm-devel(major) = ' .. version .. '\n')
    llvm_supported_versions = llvm_supported_versions .. ' ' .. version
  end
end
rpm.define(llvm_supported_versions)
}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  go-rpm-macros
BuildRequires:  llvm-devel(major)
BuildRequires:  make
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

# Set current LLVM paths.
rm llvm_config_linux*.go
for version in %{llvm_supported_versions}; do
    # Extra checks because of https://bugzilla.redhat.com/show_bug.cgi?id=1871659
    if type llvm-config-${version}-%{__isa_bits}; then
        LLVM_CONFIG=llvm-config-${version}-%{__isa_bits}
    elif type llvm-config-${version}; then
        LLVM_CONFIG=llvm-config-${version}
    elif type llvm-config-%{__isa_bits}; then
        LLVM_CONFIG=llvm-config-%{__isa_bits}
    elif type llvm-config; then
        LLVM_CONFIG=llvm-config
    else
        echo "Unable to determine llvm-config for LLVM ${version}"
        exit 1
    fi
    LLVM_CPPFLAGS=$(${LLVM_CONFIG} --cppflags)
    if [ ${version} -gt 15 ]; then
        LLVM_CPP_STD="c++17"
    else
        LLVM_CPP_STD="c++14"
    fi
    LLVM_COMPONENTS="all-targets analysis asmparser asmprinter bitreader bitwriter codegen core coroutines debuginfodwarf executionengine instrumentation interpreter ipo irreader linker mc mcjit objcarcopts option profiledata scalaropts support target"
    LLVM_LDFLAGS=$(${LLVM_CONFIG} --ldflags --libs --system-libs ${LLVM_COMPONENTS} | tr '\n' ' ')

    cat > llvm_config_linux_llvm${version}.go << EOF
//go:build !byollvm && linux && llvm${version}
// +build !byollvm,linux,llvm${version}

package llvm

// #cgo CPPFLAGS: ${LLVM_CPPFLAGS}
// #cgo CXXFLAGS: -std=${LLVM_CPP_STD}
// #cgo LDFLAGS: ${LLVM_LDFLAGS}
import "C"

type run_build_sh int
EOF
done

%install
%gopkginstall
%if %{with check}
%global gotestflags %gocompilerflags -tags="${TAGS}"
%oreon_autofiles main

%check

for version in %{llvm_supported_versions}; do
export TAGS=llvm${version}
%gocheck
done
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
