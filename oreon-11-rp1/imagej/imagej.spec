%global source3_hash d2682786a077034eac6549fad79fe6a5e1b8d8d74e81ac9413c88dbf8a36aec5
%global source2_hash 92d77739cc5f5fd1fdab5e5f893d1f3396e6c5e7f6ef9808b5b83acb4d1b8464
%global source0_hash 7134c6cb6dbe3368f297b909727c16afee34b81878c6f8edecae98aa337f5dfb
Name:           imagej
Version:        1.54r
Release:        1%{?dist}
Summary:        Image Processing and Analysis in Java
License:        LicenseRef-Fedora-Public-Domain
URL:            https://imagej.net/ij/index.html
Source0:        https://%{name}.net/ij/download/src/ij154r-src.zip
Source1:        imagej.desktop
Source2:        https://imagej.net/ij/macros/macros.zip
Source3:        https://imagej.net/ij/download/linux/unix-script.txt
Source4:        imagej.png
Source5:        DISCLAIMER
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Patch1:         imagej-1.54g-do-not-copy-class-files.patch
Patch2:         imagej-1.53r-unix-script.patch
Patch3:         imagej-1.53r-source-target-version.patch
Requires:       jpackage-utils
Requires:       java-25-devel
Obsoletes:      imagej-javadoc < 1.53r-1
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  desktop-file-utils
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
# /oreon:deps
%description
ImageJ is a public domain Java image processing program. It can display, edit,
analyze a wide variety of image data, including image sequences. Imagej can be
used for quantitative analysis of engineering and scientific image data.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -N
unzip -qq -u '%{SOURCE2}'
cp -p '%{SOURCE3}' ./imagej.sh
cp -p '%{SOURCE5}' .

# Erase binary and useless files
rm -rvf macros/.FBC* macros/build.xml __MACOSX
# Strip out any bundled pre-compiled class or jar files:
find . \( -name '*.class' -o -name '*.jar' \) -print -delete
# Fix permissions
find macros -type d -exec chmod -v 0755 '{}' '+'
find macros -type f -exec chmod -v 0644 '{}' '+'

%autopatch -p1
# Replace placeholders in our patched unix-script.txt/imagej.sh.
sed -r -i \
    -e 's#@JAVADIR@#%{_javadir}#' \
    -e 's#@PKGDATADIR@#%{_datadir}/imagej#' \
    imagej.sh

# Make sure the upstream version number is set correctly, and use the initial
# numeric <pkgrel> field of the Release as the BUILD.
%global pkgrel %(echo '%{release}' | sed -r 's/[^[:digit:]].*$//')
sed -r -i \
    -e 's/(public static final String VERSION = )"[^"]+";/\1"%{version}";/' \
    -e 's/(public static final String BUILD = )"[^"]+";/\1"%{pkgrel}";/' \
    source/ij/ImageJ.java

%build

cd source
ant build
cd ..
%install
install -p -m 0644 -D source/ij.jar '%{buildroot}%{_javadir}/imagej.jar'
install -D -p -m 0644 -t '%{buildroot}%{_datadir}/pixmaps' '%{SOURCE4}'
install -D -p -m 0644 -t '%{buildroot}%{_datadir}/imagej' \
    source/build/about.jpg source/build/IJ_Props.txt
cp -rvp macros '%{buildroot}%{_datadir}/imagej/'
install -d '%{buildroot}%{_datadir}/imagej/luts' \
    '%{buildroot}%{_datadir}/imagej/plugins'
install -D -p imagej.sh '%{buildroot}%{_bindir}/imagej'
desktop-file-install --vendor=''                     \
       --dir=%{buildroot}%{_datadir}/applications/   \
       %{SOURCE1}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
