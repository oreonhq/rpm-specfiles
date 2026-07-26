%global source0_hash 21ea6ffb995312735f30e45c2e6cfb2e1654286dbd1dd2190457607df28d0c68

Name:           eblook
Version:        1.6.1
Release:        43%{?dist}
Summary:        Command-line EB and EPWING dictionary search program

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://openlab.ring.gr.jp/edict/eblook/
Source0:        http://openlab.ring.gr.jp/edict/eblook/dist/%{name}-%{version}.tar.gz
Patch0:         eblook-strcpy.patch
Patch1:         eblook-size_t.patch
Patch2:         eblook-ssize_t.patch

BuildRequires:  eb-devel
BuildRequires:	automake, libtool
BuildRequires: make

%description
Command-line EB and EPWING dictionary search program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p2
%patch -P2 -p1
for i in NEWS README; do
    iconv -f ISO-2022-JP -t UTF-8 $i > ${i}.UTF-8
    mv ${i}.UTF-8 $i
done
autoreconf -fi

%build
%configure --with-eb-conf=%{_libdir}/eb.conf
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# convert info file to utf-8
( cd $RPM_BUILD_ROOT%{_infodir}
  %{_bindir}/iconv -f EUC-JP -t UTF-8 eblook.info > eblook.info.utf8 && mv -f eblook.info{.utf8,} || rm eblook.info.utf8
)

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/eblook
%{_infodir}/eblook.info*

%changelog
%autochangelog
