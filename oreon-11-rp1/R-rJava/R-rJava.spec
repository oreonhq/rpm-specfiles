%global source0_hash b9c9e324d2846e7b3ec22992271d27252d3cd6291491931f9362bbb78bc8c355

Name:           R-rJava
Version:        %R_rpm_version 1.0-14
Release:        %autorelease
Summary:        Low-Level R to Java Interface

License:        LGPL-2.1-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-javadoc < %{version}-%{release}
ExclusiveArch:  %{java_arches}

%description
Low-level interface to Java VM very much like .C/.Call and friends.
Allows creation of objects, calling methods and accessing fields.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm rJava/inst/jri/*.jar

%generate_buildrequires
%R_buildrequires

%build
# rebuild jars
find rJava/jri/REngine -name Makefile -exec sed -i 's/1.6/1.8/g' {} \;
%make_build -C rJava/jri/REngine
%make_build -C rJava/jri/REngine/JRI
mv rJava/jri/REngine/{REngine,JRI/JRIEngine}.jar rJava/inst/jri/

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
