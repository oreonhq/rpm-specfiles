%global source0_hash 4db86e1ea82398c0396a4e157dd2f50003c5445f421fda706560f9242f13c74e

%bcond_without bootstrap

Name:           ibus-table-extraphrase
Version:        1.3.9.20110826
Release:        30%{?dist}
Summary:        Extra phrase for ibus-table
License:        GPL-3.0-or-later
URL:            http://code.google.com/p/ibus/
Source0:        http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz

BuildArch:      noarch

# for noarch pkgconfig
BuildRequires:  ibus-table-devel >= 1.1.0.20090220-5
%if %{with bootstrap}
BuildRequires:  gettext-devel >= 0.17, automake >= 1.10.2
%endif
BuildRequires: make

%description
Extra phrase data for IBus-Table engine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
export IBUS_TABLE_CREATEDB="%{_bindir}/ibus-table-createdb --no-create-index"
%if %{with bootstrap}
./autogen.sh \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
%else
%configure \
%endif

#    --enable-extraphrase
make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
make install \
  DESTDIR=%{buildroot} \
  INSTALL="install -p" \
  pkgconfigdir=%{_datadir}/pkgconfig

%files
%doc AUTHORS ChangeLog COPYING README
%{_datadir}/pkgconfig/ibus-table-extraphrase.pc
%{_datadir}/ibus-table/data/extra_phrase.txt

%changelog
%autochangelog
