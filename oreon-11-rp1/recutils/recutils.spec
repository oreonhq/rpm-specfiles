%global source0_hash 275f1d819111ffc6d84bf9c4e2ab4c4757793a5ef5b88ba0e59a8d7822fb8562

Name:		recutils
Version:	1.9
Release:	13%{?dist}
Summary:	A set of tools to access GNU recfile databases

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://www.gnu.org/software/recutils/
Source0:	https://ftp.gnu.org/gnu/recutils/%{name}-%{version}.tar.gz
Source1:	https://ftp.gnu.org/gnu/recutils/%{name}-%{version}.tar.gz.sig
Source2:	gpgkey-BDFA5717FC1DD35C2C3832A23EF90523B304AF08.gpg
# The source is generated with:
# git clone https://git.savannah.gnu.org/git/recutils/rec-mode.git
# git archive --format=tar.gz --prefix=rec-mode/ HEAD  > ../rec-mode-$(git describe).tar.gz
Source3:	rec-mode-v1.8.3.tar.gz
Source4:	rec-mode-init.el
Patch1:		recutils-1.9-mdbtools-0.9.patch
Patch2:		recutils-c99.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	gettext
BuildRequires:	emacs-nox
BuildRequires:	chrpath
BuildRequires:	libgcrypt-devel
BuildRequires:	help2man
BuildRequires:	mdbtools-devel
BuildRequires:	texinfo
BuildRequires:	gnupg2
BuildRequires:  bison flex
Requires:	emacs(bin) >= %{_emacs_version}
# Gnulib is granted exception of "no bundled libraries" packaging guideline:
# https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_exceptions
Provides: bundled(gnulib)

%description
Recutils is a set of tools and libraries to access human-editable,
text-based databases called recfiles. The data is stored as a sequence
of records, each record containing an arbitrary number of named
fields.

%package devel
Summary:	Libraries and header files for recutils
Requires:	%{name} = %{version}-%{release}

%description devel
Libraries and header files for recutils

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# mdbtools >= 0.9.0 no longer has mdb_init
sed -i 's/mdb_init/mdb_open/' configure
tar xf %{SOURCE3}

%build
%configure --disable-static --disable-rpath
%make_build
%{_emacs_bytecompile} rec-mode/*.el

%check
make check

%install
%make_install INSTALL="install -p"

# install Emacs mode
install -dm 755 %{buildroot}%{_emacs_sitelispdir}
install -pm 644 rec-mode/*.el* %{buildroot}%{_emacs_sitelispdir}

# install startup file for the Emacs mode installed above
install -dm 755 %{buildroot}/%{_emacs_sitestartdir}
install -pm 644 %{SOURCE4} %{buildroot}/%{_emacs_sitestartdir}

# install info files for Emacs mode
install -pm 644 rec-mode/rec-mode.info %{buildroot}%{_infodir}

rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/*.la

chrpath --delete %{buildroot}%{_bindir}/*

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_libdir}/*.so.*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/recutils
%{_infodir}/*.info*
%{_emacs_sitelispdir}/*.el*
%{_emacs_sitestartdir}/*.el

%files devel
%{_includedir}/rec.h
%{_libdir}/*.so

%changelog
%autochangelog
