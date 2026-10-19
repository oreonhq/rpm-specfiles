%global source1_hash d3b9bbd3a52a4e68cfee626f18e329520d61902e51c75392024c78cdae8f60c8
%global source0_hash 665c241c42920bf369f1231d4b9c71ce18ba63add0b9a8f241821fd11a28d592
%global       debug_package %{nil}
%global       mver 3.0
Name:         skribilo
Version:      0.11.1
Release:        1%{?dist}
Summary:        A free document production tool
License:      GPL-3.0-or-later
URL:          https://www.nongnu.org/%{name}
Source0:        https://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:      https://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz.sig
Source2:      arunisaac.pub
Requires:       guile30
Requires:       lomt-junction-fonts
Requires:       linux-libertine-biolinum-fonts
Requires:       linux-libertine-fonts
Requires:       source-foundry-hack-fonts
Requires:       texlive-lobster2
# oreon:deps
BuildRequires:  ImageMagick-devel
BuildRequires:  emacs
BuildRequires:  gettext-devel
BuildRequires:  glibc-common
BuildRequires:  glibc-devel
BuildRequires:  gnupg2
BuildRequires:  guile-reader-devel
BuildRequires:  guile30-devel
BuildRequires:  lout
BuildRequires:  make
BuildRequires:  texlive
BuildRequires:  texlive-collection-context
# /oreon:deps
%description
Skribilo is a free document production tool that takes a structured document 
representation as its input and renders that document in a variety of output
formats: HTML and Info for on-line browsing, and Lout and LaTeX for
high-quality hard copies.

The input document can use Skribilo's markup language to provide information
about the document's structure, which is similar to HTML or LaTeX and does not
require expertise. Alternatively, it can use a simpler, “markup-less” format
that borrows from Emacs' outline mode and from other conventions used in
emails, Usenet and text.

Last but not least, Skribilo can be thought of as a complete document
programming framework for the Scheme programming language that may be used to
automate a variety of document generation tasks. Technically, the Skribilo
language/API is an embedded domain-specific language (EDSL), implemented via
so-called “deep embedding”. Skribilo uses GNU Guile 3.0 or 2.x as the
underlying Scheme implementation.

%package emacs
Summary:  Skribilo Emacs configuration
Requires:        skribilo
Requires:        emacs
BuildArch: noarch
%description emacs
Configuration files for writing Skribilo documents using
Emacs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

iconv -f ISO-8859-1 -t UTF-8 ChangeLog.Skribe > ChangeLog.Skribe.tmp
rm ChangeLog.Skribe
mv ChangeLog.Skribe.tmp ChangeLog.Skribe
iconv -f ISO-8859-1 -t UTF-8 doc/man/skribilo.1.in > doc/man/skribilo.1.in.tmp
rm doc/man/skribilo.1.in
mv doc/man/skribilo.1.in.tmp doc/man/skribilo.1.in

%build

%configure --with-guilemoduledir=%{_datadir}/guile/site/%{mver}
%make_build
%install
%make_install
rm %{buildroot}%{_infodir}/*.png
for i in %{buildroot}%{_docdir}/%{name}/*.png; do \
  (cd %{buildroot}%{_infodir}; \
   ln -sf -r "$i" . ); \
done
rm %{buildroot}/%{_docdir}/%{name}/*.pdf
rm -f %{buildroot}%{_docdir}/%{name}/junction.ttf
ln -sf /usr/share/fonts/Junction-regular.otf  %{buildroot}%{_docdir}/%{name}/Junction-regular.otf
rm -f %{buildroot}%{_docdir}/%{name}/lobster-2.100.otf
ln -sf /usr/share/fonts/lobster2/LobsterTwo-Regular.otf %{buildroot}%{_docdir}/%{name}/LobsterTwo-Regular.otf
rm -f %{buildroot}%{_docdir}/%{name}/static/Hack-Regular.ttf
ln -sf /usr/share/fonts/source-foundry-hack-fonts/Hack-Regular.ttf %{buildroot}%{_docdir}/%{name}/static/Hack-Regular.ttf
rm -f %{buildroot}%{_docdir}/%{name}/static/LinBiolinum_Rah.ttf
ln -sf /usr/share/fonts/linux-libertine/LinBiolinum_R.otf %{buildroot}%{_docdir}/%{name}/static/LinBiolinum_R.otf
rm -f %{buildroot}%{_docdir}/%{name}/static/LinLibertine_Rah.ttf
ln -sf /usr/share/fonts/linux-libertine/LinLibertine_R.otf %{buildroot}%{_docdir}/%{name}/static/LinLibertine_R.otf
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check  

make check
%files -f %{oreon_filedir}/main.list
%files -n skribilo-emacs -f %{oreon_filedir}/skribilo-emacs.list

%changelog

%autochangelog
