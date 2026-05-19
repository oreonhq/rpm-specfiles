Name:           shared-desktop-ontologies
Version:        0.11.0
Release:        5%{?dist}
Summary:        Shared ontologies needed for semantic environments

Group:          User Interface/Desktops
# see LICENSE.README
License:        (BSD or CC-BY) and CC-BY and W3C
URL:            http://oscaf.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/oscaf/shared-desktop-ontologies/%{version}/shared-desktop-ontologies-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  cmake >= 2.6.0
BuildRequires:  pkgconfig


%description
The vision of the Social Semantic Desktop defines a user’s personal
information environment as a source and end-point of the Semantic Web:
Knowledge workers comprehensively express their information and data
with respect to their own conceptualizations.

Semantic Web languages and protocols are used to formalize these
conceptualizations and for coordinating local and global information
access. The Resource Description Framework serves as a common data
representation format. With a particular focus on addressing certain
limitations of RDF, a novel representational language akin to RDF and
the Web Ontology Language, plus a number of other high-level
ontologies were created.

Together, they provide a means to build the semantic bridges necessary
for data exchange and application integration on distributed social
semantic desktops. Although initially designed to fulfill requirements
for the Nepomuk project, these ontologies are useful for the semantic
web community in general.



%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       cmake
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries
and header files for developing applications
that use %{name}.


%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
# verify pkg-config version (notoriously wrong in recent releases)
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig
test "$(pkg-config --modversion shared-desktop-ontologies)" = "%{version}"


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS README
%doc LICENSE.README
%doc LICENSE.BSD LICENSE.CC-BY LICENSE.DCMI LICENSE.w3c
%{_datadir}/ontology/

%files devel
%defattr(-,root,root,-)
%{_datadir}/cmake/SharedDesktopOntologies/
%{_datadir}/pkgconfig/shared-desktop-ontologies.pc


%changelog
* Mon May 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11.0-5
- Import from Fedora dist-git (pre-removal), debrand
