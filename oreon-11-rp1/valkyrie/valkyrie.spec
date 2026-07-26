%global source0_hash a70b9ffb2409c96c263823212b4be6819154eb858825c9a19aad0ae398d59b43

Name:		valkyrie
Version:	2.0.0
Release:	35%{?dist}
Summary:	Graphical User Interface for Valgrind Suite

%global valkyrie %{name}-%{version}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://www.valgrind.org/
Source0:	http://www.valgrind.org/downloads/%{valkyrie}.tar.bz2
Source1:	%{name}.desktop
Patch1:		%{name}-docdir.patch
Patch2:		%{name}-usleep.patch
Patch3:		%{name}-getuid.patch
Patch4:		%{name}-getpid.patch

BuildRequires: make
BuildRequires:	desktop-file-utils
BuildRequires:	qt4-devel >= 4.2
Requires:	valgrind >= 3.6.0

%description
Valkyrie is a graphical user interface to the Valgrind suite
of tools for debugging and profiling programs.  It makes use
of the XML output capabilities offered by Valgrind.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
%{qmake_qt4} PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make INSTALL_ROOT=%{buildroot} install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -d %{buildroot}%{_datadir}/pixmaps/
install -m 644 %{_builddir}/%{valkyrie}/icons/%{name}.xpm %{buildroot}%{_datadir}/pixmaps/
cp -p %{_builddir}/%{valkyrie}/COPYING %{buildroot}%{_docdir}/%{valkyrie}
cp -p %{_builddir}/%{valkyrie}/INSTALL %{buildroot}%{_docdir}/%{valkyrie}
cp -p %{_builddir}/%{valkyrie}/README  %{buildroot}%{_docdir}/%{valkyrie}

%files
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_docdir}/%{valkyrie}

%changelog
%autochangelog
