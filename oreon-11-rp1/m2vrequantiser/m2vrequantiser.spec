%global source0_hash e537c7894edc4ae446d71e8f597aa1fcec85c3e76748ba0aaa289cc667c94209

%global srcname M2VRequantiser

Name:           m2vrequantiser
Epoch:          1
Version:        1.1
Release:        13%{?dist}
Summary:        MPEG-2 stream requantizer

License:        GPL-2.0-or-later
URL:            https://launchpad.net/m2vrequantiser
Source:         %{url}/trunk/%{version}/+download/%{srcname}-v%{version}.tar.gz
Patch:          make_dest_strip.patch

BuildRequires:  gcc
BuildRequires:  make

%description
M2VRequantiser is a tool to requantize MPEG-2 streams without
recompressing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-v%{version}

%build
%make_build

%install
%make_install PREFIX="%{_prefix}"

%files
%doc README.txt
%license LICENSE.txt
%{_bindir}/%{srcname}

%changelog
%autochangelog
