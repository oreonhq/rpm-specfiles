%global source0_hash 63ea75d4f38b34e3d20a8c9978645ac0d9e8061ea52202f9d73b337d4f8799ae

Name:           PragmARC
Version:        20130728
Release:        41%{?dist}
Summary:        PragmAda Reusable Components, a component library for Ada
Summary(sv):    PragmAda Reusable Components, ett komponentbibliotek för ada

License:        GPL-2.0-or-later WITH GNAT-exception
URL:            https://pragmada.x10hosting.com/pragmarc.htm
Source1:        https://www.Rombobjörn.se/PragmARC/pragmarc-%{version}.zip
Source2:        build_pragmarc.gpr
Source3:        pragmarc.gpr

BuildRequires:  gcc-gnat fedora-gnat-project-common >= 3
BuildRequires:  gprbuild
BuildRequires:  unzip dos2unix
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
The PragmAda Reusable Components (PragmARCs) is a library of containers, \
algorithms and utility components for Ada, ranging from the basic-but-essential \
to the high-level.

%global common_description_sv \
PragmAda Reusable Components (PragmARC) är ett bibliotek med behållare, \
algoritmer och nyttiga komponenter för ada. Det innehåller såväl grundläggande \
byggstenar som högnivåkomponenter.

%description %{common_description_en}

%description -l sv %{common_description_sv}

%package devel
Summary:        Development files for %{name}
Summary(sv):    Filer för programmering med %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common >= 2

%description devel %{common_description_en}

The %{name}-devel package contains source code and linking information for
developing applications that use %{name}.

%description devel -l sv %{common_description_sv}

Paketet %{name}-devel innehåller källkod och länkningsinformation som behövs
för att utveckla program som använder %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -T
unzip %{SOURCE1}
chmod --recursive u=rwX,go=rX .
cp -p %{SOURCE2} .

%build
# Delete files that won't be used.
rm compile_all.adb assertion_handler.adb
# Compile the library.
gprbuild -P build_pragmarc.gpr %{GPRbuild_optflags} -XDESTDIR=build_target
# Convert line breaks.
dos2unix --keepdate license.txt readme.txt arc_list.txt design.txt Test/*

%install
mv build_target/* --target-directory=%{buildroot}
# Add the project file for projects that use this library.
mkdir --parents %{buildroot}%{_GNAT_project_dir}
cp -p %{SOURCE3} %{buildroot}%{_GNAT_project_dir}/

%files
%license license.txt gpl.txt
%{_libdir}/*.so.*

%files devel
%doc readme.txt arc_list.txt design.txt Test
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pragmarc
%{_GNAT_project_dir}/*

%changelog
%autochangelog
