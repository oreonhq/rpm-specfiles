%global source0_hash 1b2e50b08a5c472237020ff4cc367beda7889dca3be1e854247f28f3af1662e2
%global	gem_name	rabbit
%define	BothRequires() \
Requires:	%1 \
%{nil}
Name:		rubygem-%{gem_name}
Version:	4.0.1
Release:        2%{?dist}
Summary:        RD-document-based presentation application
License:	GPL-2.0-or-later AND W3C AND HPND AND CC-BY-3.0
URL:		http://rabbit-shocker.org/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{name}-%{version}-test-missing-files.tar.gz
Source2:	rabbit-create-missing-test-files.sh
Source10:	rabbit.desktop
Source11:	rabbit.xml
%BothRequires	ruby(release)
Requires:	ruby(rubygems)
%BothRequires	rubygem(coderay)
%BothRequires	rubygem(csv)
%BothRequires	rubygem(drb)
%BothRequires	rubygem(gettext)
%BothRequires	rubygem(gdk_pixbuf2)
%BothRequires	rubygem(gtk3)
%BothRequires	rubygem(hikidoc)
%BothRequires	rubygem(kramdown)
Requires:	rubygem-kramdown >= 2.0
%BothRequires	rubygem(kramdown-parser-gfm)
%BothRequires	rubygem(nokogiri)
%BothRequires	rubygem(poppler)
%BothRequires	rubygem(ostruct)
%BothRequires	rubygem(rouge)
%BothRequires	rubygem(rsvg2)
%BothRequires	rubygem(rdtool)
%BothRequires	rubygem(rttool)
%BothRequires	rubygem(rexml)
Requires:	rubygem(net-irc)
Requires:	rubygem(gdk_pixbuf2) >= 3.0.9
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  ruby(release)
BuildRequires:  rubygem(coderay)
BuildRequires:  rubygem(csv)
BuildRequires:  rubygem(drb)
BuildRequires:  rubygem(gdk_pixbuf2)
BuildRequires:  rubygem(gettext)
BuildRequires:  rubygem(gtk3)
BuildRequires:  rubygem(hikidoc)
BuildRequires:  rubygem(kramdown)
BuildRequires:  rubygem(kramdown-parser-gfm)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygem(ostruct)
BuildRequires:  rubygem(poppler)
BuildRequires:  rubygem(racc)
BuildRequires:  rubygem(rdtool)
BuildRequires:  rubygem(rexml)
BuildRequires:  rubygem(rouge)
BuildRequires:  rubygem(rsvg2)
BuildRequires:  rubygem(rttool)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(test-unit-notify)
BuildRequires:  rubygem(test-unit-rr)
BuildRequires:  rubygems-devel
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
Rabbit is an RD-document-based presentation application.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gem_name}-%{version} -a 1 -p 1
mv ../%{gem_name}-%{version}.gemspec .

# Remove gtk4 dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*gtk4@d'

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
cp -a %{gem_name}-%{version}/test/ ./%{gem_instdir}/
%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
	%{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
mkdir -p -m 0755 \
	%{buildroot}%{_datadir}/{applications/,mime/packages/}
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications/ \
	%{SOURCE10}
install -cpm 644 %{SOURCE11} %{buildroot}%{_datadir}/mime/packages/
mkdir -p -m 0755 \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
install -cpm 644 .%{gem_instdir}/sample/rabbit_icon.png \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Gemfile \
	Rakefile \
	%{gem_name}.gemspec \
	po/ \
	test/ \
	%{nil}
popd
%find_lang rabbit
find %{buildroot}%{gem_instdir}/data/locale -type d | while read dir
do
	echo "%%dir ${dir#%{buildroot}}" >> rabbit.lang
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LANG=C.utf8
pushd .%{gem_instdir}
sed -i.skip test/parser/test-markdown.rb \
	-e 's|\(def test_codeblock_fence\)|\1 ; omit|'
xvfb-run \
	ruby test/run-test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rabbit-doc -f %{oreon_filedir}/rubygem-rabbit-doc.list

%changelog

%autochangelog
