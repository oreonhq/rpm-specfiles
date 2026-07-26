%global source0_hash ee9538fce98895dcf0d108087d3ee2e13f5c08ed94c983f0218a7a3d153b725d

Name:		progress
Version:	0.17
Release:	6%{?dist}
Summary:	Coreutils Viewer

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/Xfennec/%{name}
Source0:	https://github.com/Xfennec/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	ncurses-devel

%if (0%{?fedora} && 0%{?fedora} <= 26) || (0%{?rhel} && 0%{?rhel} <= 9)
Obsoletes: cv <= 0.8-3
Provides: cv == %{version}-%{release}
%endif # (0%{?fedora} && 0%{?fedora} <= 26) || (0%{?rhel} && 0%{?rhel} <= 9)

%description
Progress can be described as a Tiny Dirty Linux Only* C command that
looks for coreutils basic commands (cp, mv, dd, tar, gzip/gunzip, cat, ...)
currently running on your system and displays the percentage of copied data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
CFLAGS="%{?optflags}"			\
LFLAGS="%{?__global_ldflags}"	\
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 %{name} %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 *.1 %{buildroot}%{_mandir}/man1

%files
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
%license LICENSE
%else  # 0%{?fedora} >= 21 || 0%{?rhel} >= 8
%doc LICENSE
%endif # 0%{?fedora} >= 21 || 0%{?rhel} >= 8
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1*

%changelog
%autochangelog
