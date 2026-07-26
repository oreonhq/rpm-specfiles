%global source0_hash 56284001f40da9854e56215527e292de4811ce349e27d7a3e8add35c72da2f95

Summary:        Extension for creating pdf-Files with CUPS
Summary(fr):    Extension de CUPS pour créer des fichiers PDF
Name:           cups-pdf
Version:        3.0.2
Release:        3%{?dist}
URL:            https://www.cups-pdf.de/
License:        GPL-2.0-or-later

Source0:        https://www.cups-pdf.de/src/%{name}_%{version}.tar.gz
Source1:        INSTALL.fedora.cups-pdf

# Default value for Out ${DESKTOP}
Patch1:         cups-pdf-conf.patch
# Handle ${DESKTOP} from config
Patch2:         cups-pdf-desktop.patch
# Handle new lines in title
Patch3:         cups-pdf-title.patch
# Fix build warning
Patch4:         cups-pdf-build.patch
# Report error/success in log
Patch5:         cups-pdf-result.patch
# Fix processing of lines with embedded null characters
Patch6:         cups-pdf-fix-null-chars.patch

BuildRequires:  gcc
BuildRequires:  cups-devel

Requires:       ghostscript, cups
Requires(post): %{_bindir}/pgrep

# These are the defaults paths defined in config.h
# CUPS-PDF spool directory
%global CPSPOOL   %{_localstatedir}/spool/cups-pdf/SPOOL

# CUPS-PDF output directory
%global CPOUT     %{_localstatedir}/spool/cups-pdf

# CUPS-PDF log directory
%global CPLOG     %{_localstatedir}/log/cups

# CUPS-PDF cups-pdf.conf config file
%global ETCCUPS   %(cups-config --serverroot 2>/dev/null || echo %{_sysconfdir}/cups)

# Additional path to backend directory
%global CPBACKEND %(cups-config --serverbin  2>/dev/null || echo %{_libdir}/cups)/backend

%description
"cups-pdf" is a backend script for use with CUPS - the "Common UNIX Printing
System" (see more for CUPS under https://www.cups.org/).
"cups-pdf" uses the ghostscript pdfwrite device to produce PDF Files.

This version has been modified to store the PDF files on the Desktop of the
user. This behavior can be changed by editing the configuration file.

%description -l fr
"cups-pdf" est un script de traitement CUPS - le "Common UNIX Printing System"
(plus d'informations sur CUPS à l'adresse https://www.cups.org/).
"cups-pdf" utilise ghostscript pour construire des fichiers au format PDF.

Cette version a été modifiée pour produire les fichiers PDF sur le bureau
de l'utilisateur (dossier Desktop du répertoire d'accueil de l'utilisateur).
Ce comportement peut être modifié en éditant le fichier de configuration.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

echo CIBLE = %{name}-%{version}-%{release}
%setup -q -n %{name}-%{version}
cp -p %{SOURCE1} INSTALL.RPM

%patch -P1 -p0 -b .oldconf
%patch -P2 -p0 -b .desktop
%patch -P3 -p0 -b .title
%patch -P4 -p0 -b .build
%patch -P5 -p0 -b .result
%patch -P6 -p1 -b .nullchars

%build
pushd src
%{__cc} $RPM_OPT_FLAGS $RPM_LD_FLAGS -D_GNU_SOURCE -o cups-pdf cups-pdf.c -lcups
popd

%install
mkdir -p %{buildroot}%{CPBACKEND}
mkdir -p %{buildroot}%{CPSPOOL}
mkdir -p %{buildroot}%{CPOUT}
mkdir -p %{buildroot}%{CPLOG}
mkdir -p %{buildroot}%{CPBACKEND}
mkdir -p %{buildroot}%{ETCCUPS}
mkdir -p %{buildroot}%{_datadir}/cups/model/
install -p -m644 extra/{CUPS-PDF_noopt,CUPS-PDF_opt}.ppd  %{buildroot}%{_datadir}/cups/model/
install -p -m644 extra/cups-pdf.conf %{buildroot}%{ETCCUPS}/
install -p -m700 src/cups-pdf %{buildroot}%{CPBACKEND}/

%post
# First install : create the printer if cupsd is running
if [ "$1" -eq "1" ] && %{_bindir}/pgrep -u root -f %{_sbindir}/cupsd >/dev/null
then
    /usr/sbin/lpadmin -p Cups-PDF -v cups-pdf:/ -m CUPS-PDF_noopt.ppd -E || :
fi

%postun
if [ "$1" -eq "0" ]; then
    # Delete the printer
    /usr/sbin/lpadmin -x Cups-PDF || :
fi

%files
%license COPYING
%doc ChangeLog README INSTALL.RPM
%dir %{CPSPOOL}
%dir %{CPOUT}
%attr(700, root, root) %{CPBACKEND}/cups-pdf
%config(noreplace) %{ETCCUPS}/cups-pdf.conf
%{_datadir}/cups/model/CUPS-PDF_noopt.ppd
%{_datadir}/cups/model/CUPS-PDF_opt.ppd

%changelog
%autochangelog
