%global source0_hash 7e72b62a8a60aff5200a047eea0773a8fb205caf7acbe1774d95147f305a2f41

Summary:        Real-time file compressor
Name:           lzop
Version:        1.04
Release:        18%{?dist}
License:        GPL-2.0-or-later
URL:            https://www.lzop.org/
Source0:        https://www.lzop.org/download/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  lzo-devel
BuildRequires:  make

%description
lzop is a compression utility which is designed to be a companion to gzip.
It is based on the LZO data compression library and its main advantages over
gzip are much higher compression and decompression speed at the cost of some
compression ratio. The lzop compression utility was designed with the goals
of reliability, speed, portability and with reasonable drop-in compatibility
to gzip.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build
%configure
%make_build

%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%files
%license COPYING
%doc AUTHORS NEWS README THANKS
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.04-18
- Prepare for Oreon 11 (RP1)
