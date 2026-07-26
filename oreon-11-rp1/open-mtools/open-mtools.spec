%global source0_hash 5db4d94f7628cabe794ecf0ed3eb1e9d4cfe312a6150971e0d046a1d122d4154

%global tarname mtools
Name:       open-%{tarname}
Version:    1.0
Release:    28%{?dist}
Summary:    Tools for testing IP multicast
# README.txt:           Public Domain
# mpong.c:              BSD
# TestNet/docbook.css:  BSD
# Automatically converted from old format: Public Domain and BSD - review is highly recommended.
License:    LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-BSD
URL:        https://marketplace.informatica.com/solutions/informatica_%{tarname}
# The source repository does not exist on Google Code anymore.
# The homepage requires a registration for a download.
# The are some imports on Github like
# <https://github.com/landtuna/open-mtools.
# There also exists similar <https://github.com/troglobit/mtools>.
Source0:    https://%{name}.googlecode.com/files/%{tarname}.%{version}.zip
BuildRequires:  coreutils
BuildRequires:  gcc

%description
This package contains the msend, mdump, and mpong tools to aid in testing
multicast networks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{tarname}
# Delete precompiled binaries
rm -r AIX-* Darwin-* FreeBSD-* Linux-* SunOS-* Win2k-*
# Fix EOLs
for F in README.txt; do
    tr -d "\r" < "$F" > "${F}.unix"
    touch -r "$F" "${F}.unix"
    mv "${F}.unix" "${F}"
done

%build
for F in *.c; do
    cc %{optflags} %{?__global_ldflags} "$F" -o "${F%.c}" \
        $(test "$F" = 'mpong.c' && printf -- '-lm')
done

%install
install -d %{buildroot}%{_bindir}
for F in *.c; do
    install -t %{buildroot}%{_bindir} "${F%.c}"
done

%files
%doc README.txt TestNet/*
%{_bindir}/*

%changelog
%autochangelog
