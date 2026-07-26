%global source0_hash b4bf58401e30814382c825b13a4c3eea8ca29c314ed5c4a1f43459b78ed6f98b

Name:           seaview
Version:        5.1
Release:        4%{?dist}
Summary:        Graphical multiple sequence alignment editor
License:        GPL-3.0-or-later
URL:            http://doua.prabi.fr/software/seaview
Source0:        ftp://pbil.univ-lyon1.fr/pub/mol_phylogeny/seaview/archive/seaview_5.1.tar.gz
Source1:        seaview.desktop
Patch0:         seaview-chris.patch
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  fltk-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libXinerama-devel

%description
SeaView is a graphical multiple sequence alignment editor developed by Manolo
Gouy.  SeaView is able to read and write various alignment formats (NEXUS, MSF,
CLUSTAL, FASTA, PHYLIP, MASE).  It allows to manually edit the alignment, and
also to run DOT-PLOT or CLUSTALW/MUSCLE programs to locally improve the
alignment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n seaview
%patch -P0 -p 1 -b .chris

%build
make %{?_smp_mflags}

%check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/seaview
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 755 seaview $RPM_BUILD_ROOT/%{_bindir}
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
  --vendor fedora \
%endif
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
install -m 0644 -p seaview.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/seaview.xpm
install -m 0644 -p seaview.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/seaview.svg
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata/
install -m 0644 -p seaview.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/seaview.appdata.xml
install -m 644 seaview.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%files
%doc seaview.1.xml seaview.html
%{_bindir}/seaview
%{_datadir}/seaview/
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man1/*

%changelog
%autochangelog
