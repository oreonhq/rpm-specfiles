%global source0_hash 710df5e218a29a2500ed973c81879514b5618df01687373a3467a05f63fe8002
%bcond check 0
%ifarch x86_64
%bcond rocm 1
%else
%bcond rocm 0
%endif
ExcludeArch:    ppc64le s390x
%bcond next 0
%bcond systemd 1
%global goipath         github.com/ollama/ollama
Version:                0.12.11
%gometa -L -f
Name:           ollama
Release:        1%{?dist}
Summary:        Get up and running with OpenAI gpt-oss, DeepSeek-R1, Gemma 3 and other models
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSD-3-Clause-HP AND BSL-1.0 AND CC-BY-3.0 AND CC-BY-4.0 AND CC0-1.0 AND ISC AND LicenseRef-Fedora-Public-Domain AND LicenseRef-scancode-protobuf AND MIT AND NCSA AND NTP AND OpenSSL AND ZPL-2.1 AND Zlib
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
%if %{with systemd}
Source10:       ollama.service
Source11:       ollama.sysusers
%endif
Patch1:         0001-ollama-handle-load.patch
%if %{with rocm}
Requires:       hipblas
Requires:       rocblas
%endif
%if %{with systemd}
%{?systemd_requires}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Get up and running with OpenAI gpt-oss, DeepSeek-R1, Gemma 3 and other models.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

# Rename README's
mv app/README.md app-README.md
mv integration/README.md integration-README.md
mv llama/README.md llama-README.md

%build

%cmake \
%if %{with rocm}
    -DCMAKE_HIP_COMPILER=%rocmllvm_bindir/clang++ \
    -DAMDGPU_TARGETS=%{rocm_gpu_list_default}
%endif
%cmake_build
%global gomodulesmode GO111MODULE=on
export LDFLAGS=
%gobuild -o %{gobuilddir}/bin/ollama %{goipath}
%install
%cmake_install
runtime_removal="hipblas rocblas amdhip64 rocsolver amd_comgr hsa-runtime64 rocsparse tinfo rocprofiler-register drm drm_amdgpu numa elf"
for rr in $runtime_removal; do
    rm -rf %{buildroot}%{_prefix}/lib/ollama/lib${rr}*
done
rm -rf %{buildroot}%{_prefix}/lib/ollama/rocblas
mkdir -p %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/ollama %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_bindir}/*.so
%if %{with systemd}
install -p -D -m 0644 %{SOURCE10} %{buildroot}%{_unitdir}/ollama.service
install -p -D -m 0644 %{SOURCE11} %{buildroot}%{_sysusersdir}/ollama.conf
mkdir -p %{buildroot}%{_var}/lib/ollama
%endif
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%if %{with systemd}
%preun

%systemd_preun ollama.service
%post

%systemd_post ollama.service
%postun

%systemd_postun_with_restart ollama.service
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
