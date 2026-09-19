%global source0_hash b6a9a2a6eca046db707b0b2dfbf52faa629b62ba26c8224c641afae3831293d4

%global debug_package %{nil}

Name:           brise
Version:        0.38.20180515
Release:        21%{?dist}
Summary:        The official Rime schema repository

License:        GPL-3.0-only
URL:            https://rime.im/
Source0:        https://github.com/rime/brise/releases/download/brise-0.38/%{name}-%{version}.tar.gz

BuildRequires:  librime-tools
BuildRequires: make

%description
La brise: The official Rime schema repository.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}

%build
make %{?_smp_mflags}

%install
%make_install

%files
%doc README.md LICENSE ChangeLog AUTHORS
%{_datadir}/rime-data

%changelog
%autochangelog
