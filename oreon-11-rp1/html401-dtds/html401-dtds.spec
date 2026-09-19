%global source0_hash f0e51977b43d677ded28e10a40ccf1b0af6bfd6fe15deaafcd703edb0794ca26

# Note to self: like is with the HTML 2.0 and 3.2 DTDs, HTML 4.0 and 4.01
# have the same public id to their ENTITIES files.  They are not exactly the
# same in 4.0 and 4.01, but the changes are in comments only, so no need
# use a hardcoded system id.  Well, until something installs another, and
# incompatible set of entities using the same public id anyway...

%define date     19991224

Name:            html401-dtds
Version:         4.01
Release:         %{date}.12%{?dist}.28
Summary:         HTML 4.01 document type definitions

# W3C Software License for DTDs etc:
# http://www.w3.org/Consortium/Legal/IPR-FAQ-20000620#DTD
License:         W3C
URL:             http://www.w3.org/TR/1999/REC-html401-%{date}/
# Source0 generated with Source99, see comments in the script
Source0:         %{name}-%{date}.tar.bz2
Source99:        %{name}-prepare-tarball.sh
Patch0:          %{name}-catalog.patch

BuildArch:       noarch
Requires:        sgml-common
Requires(post):  /usr/bin/install-catalog
Requires(preun): /usr/bin/install-catalog

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

%post
/usr/bin/install-catalog --add \
  %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
  %{_datadir}/sgml/html/4.01/HTML4.cat >/dev/null

%preun
/usr/bin/install-catalog --remove \
  %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
  %{_datadir}/sgml/html/4.01/HTML4.cat >/dev/null || :

%files
%ghost %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc
%{_sysconfdir}/sgml/%{name}.soc
%{_datadir}/sgml/html/

%changelog
%autochangelog
