%global source0_hash 6e028aef1e8a6b3e5acef098584a7bb68708f35cfe74011b341c11fea5e4b5c3

Name:           bibutils
Version:        7.2
Release:        13%{?dist}
Summary:        Bibliography conversion tools

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://sourceforge.net/p/bibutils/home/Bibutils/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}_%{version}_src.tgz

BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  make

%description
The bibutils package converts between various bibliography
formats using a common MODS-format XML intermediate.

%package libs
Summary:        Bibutils library

%description libs
Bibutils library.

%package devel
Summary:        Development files for bibutils
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Bibutils development files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}_%{version}

%build
./configure \
    --install-dir %{buildroot}%{_bindir} \
    --install-lib %{buildroot}%{_libdir} \
    --dynamic
%make_build DISTRO_CFLAGS="%optflags" LDFLAGSIN="%{?__global_ldflags}"

xsltproc -o bibutils.1 --nonet /usr/share/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl bibutils.dbk

%install
%make_install

mkdir -p %{buildroot}%{_includedir}/%{name}
cp -p lib/*.h %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_libdir}/pkgconfig 
cp -p lib/%{name}.pc %{buildroot}%{_libdir}/pkgconfig
sed -i -e 's!\\!!g' -e 's!libdir=${prefix}/lib!libdir=%{_libdir}!' -e 's!${includedir}!${includedir}/%{name}!' %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{name}.1 %{buildroot}%{_mandir}/man1

for i in $(cd %{buildroot}%{_bindir}; ls *); do
  ln -s bibutils.1 %{buildroot}%{_mandir}/man1/$i.1
done

%files
%doc ChangeLog
%{_bindir}/*
%{_mandir}/man1/*.1*

%files libs
%license Copying
%{_libdir}/libbibutils.so.7
%{_libdir}/libbibutils.so.7.2

%files devel
%{_includedir}/%{name}
%{_libdir}/libbibutils.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
