%global source0_hash b0a5606cf4bf96d0500f240a11872164881349f3dbe7d3e23cc6e4068f5ae931

Name:           antlrworks
Version:        1.5.2
Release:        36%{?dist}
Summary:        Grammar development environment for ANTLR v3 grammars

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.antlr3.org/works
Source0:        https://github.com/antlr/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
# Fix compilation with JGoodies Forms >= 1.7.1
Patch0:         %{name}-1.5.2-jgoodies-forms_1.7.1.patch
# Add xdg-open to the list of available browsers to open the help
Patch1:         %{name}-1.5.2-browsers.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.jgoodies:jgoodies-forms)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.antlr:antlr)
BuildRequires:  mvn(org.antlr:antlr-runtime)
BuildRequires:  mvn(org.antlr:stringtemplate)
Requires:       graphviz
# Owns /usr/share/icons/hicolor
Requires:       hicolor-icon-theme
# Antlrworks requires javac
Requires:       java-25-devel >= 1:1.6.0
# Explicit requires for javapackages-tools since antlrworks-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
ANTLRWorks is a novel grammar development environment for ANTLR v3 grammars
written by Jean Bovet (with suggested use cases from Terence Parr). It combines
an excellent grammar-aware editor with an interpreter for rapid prototyping and
a language-agnostic debugger for isolating grammar errors. ANTLRWorks helps
eliminate grammar nondeterminisms, one of the most difficult problems for
beginners and experts alike, by highlighting nondeterministic paths in the
syntax diagram associated with a grammar. ANTLRWorks' goal is to make grammars
more accessible to the average programmer, improve maintainability and
readability of grammars by providing excellent grammar navigation and
refactoring tools, and address the most common questions and problems
encountered by grammar developers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

# Remove MacOSX-specific code
rm -r src/org/antlr/xjlib/appkit/app/MacOS/

# remove unnecessary dependency on deprecated parent pom
%pom_remove_parent

%pom_remove_dep com.apple:AppleJavaExtensions
%pom_change_dep com.jgoodies:forms com.jgoodies:jgoodies-forms

# remove maven-compiler-plugin configuration that's broken with Java 11
%pom_remove_plugin :maven-compiler-plugin

%build
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%jpackage_script org.antlr.works.IDE "-Xmx400m" "" antlrworks:antlr:antlr3:antlr3-runtime:jgoodies-common:jgoodies-forms:stringtemplate:stringtemplate4 %{name} false

desktop-file-install \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

install -Dpm 0644 resources/icons/app.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
for i in 16 32 64; do
  install -Dpm 0644 resources/icons/app_${i}x$i.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x$i/apps/%{name}.png
done

install -Dpm 0644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/appdata/%{name}.appdata.xml

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files -f .mfiles
%doc History.txt
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/appdata/*.appdata.xml

%changelog
%autochangelog
