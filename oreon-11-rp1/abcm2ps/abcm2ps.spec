%global source0_hash 5f02ac6203c4226cfbc6206935dca715ed7c45328535ee23e776c9da0219c822

Name:           abcm2ps
Version:        8.14.15
Release:        9%{?dist}
Summary:        A program to typeset ABC tunes into Postscript

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://moinejf.free.fr
Source0:        https://github.com/leesavide/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://sourceforge.net/projects/abcplus/files/Abcplus/abcplus_en-2024-07-10.zip
Patch0:		abcm2ps-gnu23.patch

BuildRequires:  gcc make
%description
Abcm2ps is a package which converts music tunes from ABC format to
Postscript. Based on abc2ps version 1.2.5, it was developed mainly to
print Baroque organ scores which have independent voices played on one
or many keyboards and a pedal-board. Abcm2ps introduces many
extensions to the ABC language that make it suitable for classical
music.

%package doc
Summary: Example ABC files with output
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Some sample ABC files with output as mp3, mid, and pdf.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%setup -q -a 1
%patch -P 0 -p 2

%build
%configure --enable-a4
%make_build CFLAGS="%{optflags}"

%install
make install \
     prefix=%{buildroot}%{_prefix} \
     bindir=%{buildroot}%{_bindir} \
     libdir=%{buildroot}%{_libdir} \
     datadir=%{buildroot}%{_datadir} \
     mandir=%{buildroot}%{_mandir} \
     docdir=$PWD/_docs_staging

%files 
%doc INSTALL README.md _docs_staging/abcm2ps/*
%license COPYING
%{_bindir}/abcm2ps
%{_datadir}/abcm2ps
%{_mandir}/man1/*

%files doc
%doc abcplus_en*/* 

%changelog
%autochangelog
