%global source0_hash e59dece4106beb08236e6c4c5827e0ad8a5ed0276d3444676019e19ebd0c49b9
Name:           fig2ps
Version:        1.5
Release:        1%{?dist}
Summary:        Utility for converting xfig pictures to PS/PDF
License:        GPL-2.0-or-later
URL:            http://fig2ps.sourceforge.net/
Source0:        http://downloads.sourceforge.net/fig2ps/%{name}-%{version}.tar.bz2
Patch0:         fig2ps-1.5-gv-ps-fix.patch
BuildArch:      noarch
Requires:       tex(latex) tex(dvips) ghostscript gv transfig
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl-generators
# /oreon:deps
%description
fig2ps is a perl script which converts xfig files to postscript or
PDF, using LaTeX for processing text (a capability not included in
transfig). This provides the benefit of seamless integration of
figures into documents (the font in the figures is the same as in the
text), and allows for special typesetting commands (such as
mathematical equations) to be included in figures.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build

%install
make install PREFIX=/usr DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
