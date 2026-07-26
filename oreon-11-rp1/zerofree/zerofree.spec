%global source0_hash 956bc861b55ba0a2b7593c58d32339dab1a0e7da6ea2b813d27c80f08b723867

Summary:        Utility to force unused ext2/3/4 inodes and blocks to zero
Name:           zerofree
Version:        1.1.1
Release:        16%{?dist}
License:        GPL-2.0-only
URL:            https://frippery.org/uml/
Source0:        https://frippery.org/uml/%{name}-%{version}.tgz
Source1:        https://frippery.org/uml/sparsify.c
Source2:        https://frippery.org/uml/index.html
# zerofree.sgml is the source for the man page from Debian.
# Unfortunately we cannot build this in Fedora because we do not have
# docbook-to-man, just docbook2man and db2x_docbook2man. The included
# man page was generated on a Debian system from this source.
Source3:        zerofree.sgml
Source4:        zerofree.8
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  e2fsprogs-devel

%description
zerofree is a utility to set unused filesystem inodes and blocks of an
ext2/3/4 filesystem to zero.  This can improve the compressibility and
privacy of an ext2/3/4 filesystem.

This tool was inspired by the ext2fs privacy (i.e. secure deletion)
patch described in a Linux kernel mailing list thread.

WARNING: The filesystem to be processed should be unmounted or mounted
read-only.  The tool tries to check this before running, but you
should be careful.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cp -p %{SOURCE1} %{SOURCE2} .

%build
make CC="%{__cc} $RPM_OPT_FLAGS $RPM_LD_FLAGS"
%{__cc} $RPM_OPT_FLAGS $RPM_LD_FLAGS -o sparsify sparsify.c -lext2fs

%install
install -D -p -m 755 zerofree $RPM_BUILD_ROOT%{_sbindir}/zerofree
install -D -p -m 755 sparsify $RPM_BUILD_ROOT%{_sbindir}/sparsify
install -D -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/man8/zerofree.8

%files
%license COPYING
%doc index.html
%{_sbindir}/zerofree
%{_sbindir}/sparsify
%{_mandir}/man8/zerofree.8*

%changelog
%autochangelog
