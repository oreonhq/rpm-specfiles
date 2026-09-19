%global source0_hash bb301697fcdb4b832fdd13893a5de697fb7de305a0c6dfc29b8d6e33a00a9dd6

Name:      spor
Summary:   Store file modes (permission/ownership) recursively 
Version:   1.0
Release:   34%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:   GPL-3.0-or-later
URL:       http://code.google.com/p/spor
Source0:   http://spor.googlecode.com/files/%{name}-%{version}.tar.bz2 

# Build changes
# http://code.google.com/p/spor/issues/detail?id=1
Patch0:    spor.1.patch
# Remove invalid -Wl from linker call
Patch1:    spor-1.0-Makefile.patch

BuildRequires: make
BuildRequires:  gcc
%description
Spor recursively walks into a given directory, storing file mode & ownership 
information in a flat-file database for future retrievals. It was firstly 
intended to use with backup & version control scripts, and it provides a 
simple and safe method to save and restore particular meta-data information 
of a given directory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
%patch -P0 -p1 -b .spor.1.man
%patch -P1 -p1

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__install} -D -p -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
%{__install} -D -p -m 0644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%doc readme.txt LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
