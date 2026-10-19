%global source0_hash f0e51977b43d677ded28e10a40ccf1b0af6bfd6fe15deaafcd703edb0794ca26
%define date     19991224
Name:            html401-dtds
Version:         4.01
Release:        1%{?dist}
Summary:        HTML 4.01 document type definitions
License:         W3C
URL:             http://www.w3.org/TR/1999/REC-html401-%{date}/
Source0:        %{name}-%{date}.tar.bz2
Source99:        %{name}-prepare-tarball.sh
Patch0:          %{name}-catalog.patch
BuildArch:       noarch
Requires:        sgml-common
Requires(post):  /usr/bin/install-catalog
Requires(preun): /usr/bin/install-catalog
# oreon:deps

# /oreon:deps
%description
This package provides the three HTML 4.01 DTDs (strict, frameset, and
transitional).  The DTDs are required for processing HTML 4.01
document instances using SGML tools such as OpenSP, OpenJade, or
SGMLSpm.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
%patch -P 0 -p1

%build

%install
install -dm 0755 %{buildroot}%{_datadir}/sgml/html/4.01
install -pm 0644 *.dtd *.cat *.ent *.decl %{buildroot}%{_datadir}/sgml/html/4.01
install -dm 0755 %{buildroot}%{_sysconfdir}/sgml
touch %{buildroot}%{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc
ln -s %{name}-%{version}-%{release}.soc %{buildroot}%{_sysconfdir}/sgml/%{name}.soc
%oreon_autofiles main

%post

/usr/bin/install-catalog --add \
  %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
  %{_datadir}/sgml/html/4.01/HTML4.cat >/dev/null
%preun

/usr/bin/install-catalog --remove \
  %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
  %{_datadir}/sgml/html/4.01/HTML4.cat >/dev/null || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
