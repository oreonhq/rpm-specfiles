%global source0_hash 7d5d5a87fde953dc2089746f6f6ab811d60e127b01074c97611898fb1ef1983d

%define beta_version 4
Name:           vbindiff
Version:        3.0 
Release:        0.36.beta%{beta_version}%{?dist}
Summary:        Visual binary diff

License:        GPL-2.0-or-later
URL:            http://www.cjmweb.net/%{name}/
Source0:        http://www.cjmweb.net/%{name}/%{name}-%{version}_beta%{beta_version}.tar.gz
# 2013-10-25: Submitted upstream: https://github.com/madsen/vbindiff/pull/3
Patch1:         crash-patch.diff

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel

%description
VBinDiff (Visual Binary Diff) displays files in hexadecimal
and ASCII (or EBCDIC). It can also display two files at once,
and highlight the differences between them.
Unlike diff, it works well with large files (up to 4 GB).

VBinDiff was inspired by the Compare Files function 
of the ProSel utilities by Glen Bredon, for the Apple II.

The single-file mode was inspired by the LIST utility 
of 4DOS and friends. While less provides a good line-oriented display,
it has no equivalent to LIST's hex display.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}_beta%{beta_version}
%patch -P1 -p1 -b .crash_patch

%build
%configure INSTALL="install -p"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS NEWS README README.PuTTY putty.src
%license COPYING
%{_bindir}/%{name}
%{_datadir}/man/man?/%{name}*

%changelog
%autochangelog
