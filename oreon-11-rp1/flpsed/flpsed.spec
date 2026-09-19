%global source0_hash b70bb751bd70af9893ae2369f0789fd79729d0d6d1fee6e0522c4e6f55c7cf6e

Name:          flpsed
Version:       0.7.3
Release:       27%{?dist}
Summary:       WYSIWYG pseudo PostScript editor

License:       GPL-1.0-or-later
URL:           http://flpsed.org/flpsed.html
Source0:       http://flpsed.org/%{name}-%{version}.tar.gz
Source1:       flpsed.desktop

BuildRequires:  gcc-c++
BuildRequires: fltk-devel
BuildRequires: desktop-file-utils
BuildRequires: make
Requires:      ghostscript

%description
Flpsed is a WYSIWYG pseudo PostScript editor. "Pseudo", because you can't
remove or modify existing elements of a document. Flpsed lets you add
arbitrary text lines to existing PostScript 1 documents. Added lines can later
be reedited with flpsed. Using pdftops, which is part of xpdf, one can convert
PDF documents to PostScript and also add text to them. flpsed is useful for
filling in forms, adding notes etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%files

%doc AUTHORS NEWS README ChangeLog INSTALL
%license COPYING 
%{_bindir}/*
%{_datadir}/applications/*
%{_mandir}/man1/*

%changelog
%autochangelog
