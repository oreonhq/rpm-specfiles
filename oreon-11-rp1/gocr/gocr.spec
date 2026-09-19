%global source0_hash df906463105f5f4273becc2404570f187d4ea52bd5769d33a7a8661a747b8686

Name:           gocr
Version:        0.52
Release:        18%{?dist}
Summary:        GNU Optical Character Recognition program

License:        GPL-2.0-or-later
URL:            http://jocr.sourceforge.net/
Source0:        http://www-e.uni-magdeburg.de/jschulen/ocr/gocr-%{version}.tar.gz
Patch0:         gocr-0.46-perms.patch

BuildRequires:  gcc
BuildRequires:  netpbm-devel
BuildRequires: make
# Needed for conversion programs
Requires:       gzip, bzip2, /usr/bin/djpeg, netpbm-progs, transfig
Obsoletes:      %{name}-devel <= 0.45-4

%description
GOCR is an OCR (Optical Character Recognition) program, developed under the
GNU Public License. It converts scanned images of text back to text files.
Joerg Schulenburg started the program, and now leads a team of developers.

GOCR can be used with different front-ends, which makes it very easy to port
to different OSes and architectures. It can open many different image
formats, and its quality have been improving in a daily basis.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .perms

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
# Don't ship static library
rm -rf $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_includedir}
# Don't ship buggy Tcl/Tk frontend
rm $RPM_BUILD_ROOT/%{_bindir}/gocr.tcl

%files
%doc AUTHORS BUGS CREDITS doc/gocr.html gpl.html HISTORY README
%doc REMARK.txt REVIEW TODO
%lang(de) %doc READMEde.txt
%{_bindir}/gocr
%{_mandir}/man1/gocr.1*

%changelog
%autochangelog
