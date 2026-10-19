%global source1_hash c4395261ba92e25388e58552d0022a3294778b43a6b8de0e72f8679d9d05c68b
%global source0_hash 07f731a995bcc9773f06a9f40763d8717123267d9d68fb086d513b8f4e953219
Name:           glsl-analyzer
Version:        1.7.1
Release:        1%{?dist}
Summary:        Language server for GLSL
License:        GPL-3.0-only
URL:            https://github.com/nolanderc/glsl_analyzer
ExclusiveArch:  %{zig_arches}
Source0:        https://github.com/nolanderc/glsl_analyzer/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/nolanderc/glsl-samples/archive/95264d5602cc8542e9e8dbdaab6045f9619ab180.tar.gz#/glsl-samples-95264d5.tar.gz
Patch:          0001-Add-fPIE-compiler-flag.patch
Patch:          0002-update-to-zig-0.15.2.patch
# oreon:deps
BuildRequires:  (zig >= 0.15.2 with zig < 0.16)
BuildRequires:  pytest
BuildRequires:  python3-lsprotocol
BuildRequires:  python3-pytest-lsp
BuildRequires:  python3-pytest-subtests
BuildRequires:  python3-typeguard
BuildRequires:  zig-rpm-macros
# /oreon:deps
%description
Language server for GLSL (OpenGL Shading Language).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's/b.run(&.{ "git", "describe", "--tags", "--always" })/"%{version}"/' build.zig

tar -xf %{SOURCE1} -C tests/glsl-samples --strip-components=1

%build

%zig_prep
%zig_build
%install
%zig_install
%oreon_autofiles main

%check

%ifnarch aarch64
export PATH="./zig-out/bin:${PATH}"
pytest tests
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
