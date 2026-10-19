%global source0_hash bd1b66d20a4020ab94b512e56d76cb5f86470d0216081586d596366927cb8d8b
Name:           dc3dd
Version:        7.3.1
Release:        1%{?dist}
Summary:        Patched version of GNU dd for use in computer forensics
License:        GPLv3+
URL:            http://sourceforge.net/projects/dc3dd/
Source0:        http://downloads.sourceforge.net/dc3dd/%{name}-%{version}.zip
Patch1:         dc3dd-01_automake.patch
Patch2:         dc3dd-configure-c99.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  gnulib-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  p7zip
BuildRequires:  perl(I18N::Langinfo)
BuildRequires:  perl(Locale::gettext)
BuildRequires:  readline-devel
# /oreon:deps
%description
dc3dd is a patched version of GNU dd to include a number of features useful
for computer forensics. Many of these features were inspired by dcfldd, but
were rewritten for dc3dd.

* Pattern writes. The program can write a single hexadecimal value or a
    text string to the output device for wiping purposes.
* Piecewise and overall hashing with multiple algorithms and variable 
    size windows. Supports MD5, SHA-1, SHA-256, and SHA-512. Hashes can be 
    computed before or after conversions are made.
* Progress meter with automatic input/output file size probing
* Combined log for hashes and errors
* Error grouping. Produces one error message for identical sequential 
    errors
* Verify mode. Able to repeat any transformations done to the input 
    file and compare it to an output.
* Ability to split the output into chunks with numerical or alphabetic 
    extensions

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git

#Missing x flag in version 7.2.646 makes the build fail
chmod +x build-aux/git-version-gen configure

# ChangeLog having wrong ends of lines
sed -i -e 's|\r||g' ChangeLog

%build

autoreconf -vif #BZ925238 - support aarch64
%configure 
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
