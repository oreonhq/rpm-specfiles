# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           virt-top
Version:        1.1.2
Release:        7%{?dist}
Summary:        Utility like top(1) for displaying virtualization stats
License:        GPL-2.0-or-later

%if 0%{?rhel}
# No qemu-kvm on POWER (RHBZ#1946532).
ExcludeArch:    %{power64}
%endif

URL:            https://people.redhat.com/~rjones/virt-top/
Source0:        https://people.redhat.com/~rjones/virt-top/files/%{name}-%{version}.tar.gz
Source1:        https://people.redhat.com/~rjones/virt-top/files/%{name}-%{version}.tar.gz.sig

# Post-process output of CSV file (RHBZ#665817, RHBZ#912020).
Source2:        processcsv.py
Source3:        processcsv.py.pod

# Keyring used to verify tarball signature.
Source4:        libguestfs.keyring

# Adds a link to processcsv to the man page.  This patch is only
# included in RHEL builds.
Patch1:         virt-top-1.0.9-processcsv-documentation.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ocaml >= 3.10.2
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-findlib-devel
# Need the ncurses / ncursesw (--enable-widec) fix.
BuildRequires:  ocaml-curses-devel >= 1.0.3-7
BuildRequires:  ocaml-calendar-devel
BuildRequires:  ocaml-libvirt-devel >= 0.6.1.5
BuildRequires:  ocaml-gettext-devel >= 0.3.3
BuildRequires:  ocaml-fileutils-devel
# For msgfmt:
BuildRequires:  gettext

# Non-OCaml BRs.
BuildRequires:  libvirt-devel
BuildRequires:  libxml2-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  gawk
BuildRequires:  gnupg2


%description
virt-top is a 'top(1)'-like utility for showing stats of virtualized
domains.  Many keys and command line options are the same as for
ordinary 'top'.

It uses libvirt so it is capable of showing stats across a variety of
different virtualization systems.


%prep
%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%if 0%{?rhel} >= 6
%patch -P1 -p1
%endif

# "ocamlfind byte" has been removed as an alias
sed -i 's/\(OCAMLBEST=\)byte/\1ocamlc/' configure


%build
%configure
make

# Force rebuild of man page.
# There is a missing man_MANS rule, will fix upstream in next version.
rm -f src/virt-top.1
make -C src virt-top.1

%if 0%{?rhel} >= 6
# Build processcsv.py.1.
pod2man -c "Virtualization Support" --release "%{name}-%{version}" \
  %{SOURCE3} > processcsv.py.1
%endif


%install
make DESTDIR=$RPM_BUILD_ROOT install

# Install translations.
%find_lang %{name}

# Install virt-top manpage by hand for now - see above.
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 0644 src/virt-top.1 $RPM_BUILD_ROOT%{_mandir}/man1

%if 0%{?rhel} >= 6
# Install processcsv.py.
install -m 0755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}

# Install processcsv.py(1).
install -m 0644 processcsv.py.1 $RPM_BUILD_ROOT%{_mandir}/man1/
%endif


%files -f %{name}.lang
%doc README TODO
%license COPYING
%{_bindir}/virt-top
%{_mandir}/man1/virt-top.1*
%if 0%{?rhel} >= 6
%{_bindir}/processcsv.py
%{_mandir}/man1/processcsv.py.1*
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.2-7
- Prepare for Oreon 11 (RP1)
