%global source0_hash b25dc7bf8ed093d8b6e043e88013736902c1082c958b81a598af5db5275539a5
Name:           beets
Version:        2.14.1
Release:        1%{?dist}
Summary:        Music library manager and MusicBrainz tagger
License:        MIT and ISC
URL:            http://pypi.org/project/beets/
Source0:        https://files.pythonhosted.org/packages/source/b/beets/beets-%{version}.tar.gz
BuildArch:      noarch
Requires:       python-packaging
Provides:       beets-plugins = %{version}-%{release}
Obsoletes:      beets-plugins < %{version}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-beets = %{version}-%{release}
# /oreon:deps
%package -n       python3-beets+absubmit
Summary:        Metapackage for python3-beets absubmit extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[absubmit]) = %{version}-%{release}

%description -n python3-beets+absubmit
Metapackage for python3-beets absubmit extras.

%package -n       python3-beets+aura
Summary:        Metapackage for python3-beets aura extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[aura]) = %{version}-%{release}

%description -n python3-beets+aura
Metapackage for python3-beets aura extras.

%package -n       python3-beets+autobpm
Summary:        Metapackage for python3-beets autobpm extras
Requires:       python3-beets = %{version}-%{release}
Requires:       python3dist(librosa) >= 0.11
Requires:       python3dist(resampy) >= 0.4.3
Requires:       python3dist(numba) >= 0.65.1
Provides:       python3dist(beets[autobpm]) = %{version}-%{release}

%description -n python3-beets+autobpm
Metapackage for python3-beets autobpm extras.

%package -n       python3-beets+beatport
Summary:        Metapackage for python3-beets beatport extras
Requires:       python3-beets = %{version}-%{release}
Requires:       python3dist(requests-oauthlib) >= 0.6.1
Provides:       python3dist(beets[beatport]) = %{version}-%{release}

%description -n python3-beets+beatport
Metapackage for python3-beets beatport extras.

%package -n       python3-beets+bpd
Summary:        Metapackage for python3-beets bpd extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[bpd]) = %{version}-%{release}

%description -n python3-beets+bpd
Metapackage for python3-beets bpd extras.

%package -n       python3-beets+chroma
Summary:        Metapackage for python3-beets chroma extras
Requires:       python3-beets = %{version}-%{release}
Requires:       python3dist(pyacoustid) >= 1.3.1
Requires:       python3dist(pyacoustid) < 2
Provides:       python3dist(beets[chroma]) = %{version}-%{release}

%description -n python3-beets+chroma
Metapackage for python3-beets chroma extras.

%package -n       python3-beets+discogs
Summary:        Metapackage for python3-beets discogs extras
Requires:       python3-beets = %{version}-%{release}
Requires:       python3dist(python3-discogs-client) >= 2.3.15
Provides:       python3dist(beets[discogs]) = %{version}-%{release}

%description -n python3-beets+discogs
Metapackage for python3-beets discogs extras.

%package -n       python3-beets+embedart
Summary:        Metapackage for python3-beets embedart extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[embedart]) = %{version}-%{release}

%description -n python3-beets+embedart
Metapackage for python3-beets embedart extras.

%package -n       python3-beets+embyupdate
Summary:        Metapackage for python3-beets embyupdate extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[embyupdate]) = %{version}-%{release}

%description -n python3-beets+embyupdate
Metapackage for python3-beets embyupdate extras.

%package -n       python3-beets+fetchart
Summary:        Metapackage for python3-beets fetchart extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[fetchart]) = %{version}-%{release}

%description -n python3-beets+fetchart
Metapackage for python3-beets fetchart extras.

%package -n       python3-beets+import
Summary:        Metapackage for python3-beets import extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[import]) = %{version}-%{release}

%description -n python3-beets+import
Metapackage for python3-beets import extras.

%package -n       python3-beets+kodiupdate
Summary:        Metapackage for python3-beets kodiupdate extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[kodiupdate]) = %{version}-%{release}

%description -n python3-beets+kodiupdate
Metapackage for python3-beets kodiupdate extras.

%package -n       python3-beets+lastgenre
Summary:        Metapackage for python3-beets lastgenre extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[lastgenre]) = %{version}-%{release}

%description -n python3-beets+lastgenre
Metapackage for python3-beets lastgenre extras.

%package -n       python3-beets+lastimport
Summary:        Metapackage for python3-beets lastimport extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[lastimport]) = %{version}-%{release}

%description -n python3-beets+lastimport
Metapackage for python3-beets lastimport extras.

%package -n       python3-beets+lyrics
Summary:        Metapackage for python3-beets lyrics extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[lyrics]) = %{version}-%{release}

%description -n python3-beets+lyrics
Metapackage for python3-beets lyrics extras.

%package -n       python3-beets+metasync
Summary:        Metapackage for python3-beets metasync extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[metasync]) = %{version}-%{release}

%description -n python3-beets+metasync
Metapackage for python3-beets metasync extras.

%package -n       python3-beets+mpdstats
Summary:        Metapackage for python3-beets mpdstats extras
Requires:       python3-beets = %{version}-%{release}
Requires:       python3dist(python-mpd2) >= 0.4.2
Provides:       python3dist(beets[mpdstats]) = %{version}-%{release}

%description -n python3-beets+mpdstats
Metapackage for python3-beets mpdstats extras.

%package -n       python3-beets+plexupdate
Summary:        Metapackage for python3-beets plexupdate extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[plexupdate]) = %{version}-%{release}

%description -n python3-beets+plexupdate
Metapackage for python3-beets plexupdate extras.

%package -n       python3-beets+reflink
Summary:        Metapackage for python3-beets reflink extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[reflink]) = %{version}-%{release}

%description -n python3-beets+reflink
Metapackage for python3-beets reflink extras.

%package -n       python3-beets+replaygain
Summary:        Metapackage for python3-beets replaygain extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[replaygain]) = %{version}-%{release}

%description -n python3-beets+replaygain
Metapackage for python3-beets replaygain extras.

%package -n       python3-beets+scrub
Summary:        Metapackage for python3-beets scrub extras
Requires:       python3-beets = %{version}-%{release}
Requires:       python3dist(mutagen) >= 1.33
Provides:       python3dist(beets[scrub]) = %{version}-%{release}

%description -n python3-beets+scrub
Metapackage for python3-beets scrub extras.

%package -n       python3-beets+sonosupdate
Summary:        Metapackage for python3-beets sonosupdate extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[sonosupdate]) = %{version}-%{release}

%description -n python3-beets+sonosupdate
Metapackage for python3-beets sonosupdate extras.

%package -n       python3-beets+tidal
Summary:        Metapackage for python3-beets tidal extras
Requires:       python3-beets = %{version}-%{release}
Requires:       python3dist(requests-oauthlib) >= 0.6.1
Provides:       python3dist(beets[tidal]) = %{version}-%{release}

%description -n python3-beets+tidal
Metapackage for python3-beets tidal extras.

%package -n       python3-beets+titlecase
Summary:        Metapackage for python3-beets titlecase extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[titlecase]) = %{version}-%{release}

%description -n python3-beets+titlecase
Metapackage for python3-beets titlecase extras.

%package -n       python3-beets+thumbnails
Summary:        Metapackage for python3-beets thumbnails extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[thumbnails]) = %{version}-%{release}

%description -n python3-beets+thumbnails
Metapackage for python3-beets thumbnails extras.

%package -n       python3-beets+web
Summary:        Metapackage for python3-beets web extras
Requires:       python3-beets = %{version}-%{release}
Provides:       python3dist(beets[web]) = %{version}-%{release}

%description -n python3-beets+web
Metapackage for python3-beets web extras.

%description
The purpose of beets is to get your music collection right once and for all. It
catalogs your collection, automatically improving its meta-data as it goes using
the MusicBrainz database. Then it provides a bouquet of tools for manipulating
and accessing your music.
Because beets is designed as a library, it can do almost anything you can
imagine for your music collection. Via plugins, beets becomes a panacea:
- Fetch or calculate all the meta-data you could possibly need: album art,
  lyrics, genres, tempos, ReplayGain levels, or acoustic fingerprints.
- Get meta-data from MusicBrainz, Discogs, or Beatport. Or guess meta-data using
  songs' file names or their acoustic fingerprints.
- Transcode audio to any format you like.
- Check your library for duplicate tracks and albums or for albums that are
  missing tracks.
- Browse your music library graphically through a Web browser and play it in
  any browser that supports HTML5 Audio.

%package doc
Summary:        Documentation for beets
%description doc
The beets-doc package provides useful information on the
beets Music Library Manager. Documentation is shipped in
both text and html formats.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Tarball has wrong basedir https://github.com/beetbox/beets/issues/5284
%autosetup -p1 -n beets-%{version}

# Drop optional sphinx_toolbox extension (not packaged in Fedora)
sed -i '/sphinx_toolbox.more_autodoc.autotypeddict/d' docs/conf.py

%build

%pyproject_wheel
pushd docs
env PYTHONPATH=.. sphinx-build-3 -b man  -d _build/doctrees . _build/man
env PYTHONPATH=.. sphinx-build-3 -b html -d _build/doctrees . _build/html
env PYTHONPATH=.. sphinx-build-3 -b text -d _build/doctrees . _build/text
popd
%check

PYTHONPATH=. python3 - <<'PY'
import beets
assert beets.__version__ == "%{version}", f"got {beets.__version__}"
PY
%pytest \
  --deselect test/test_importer.py::ImportDuplicateAlbumTest::test_merge_duplicate_album \
  --ignore test/plugins
%install
%pyproject_install
install -Dm0644 docs/_build/man/beet.1 \
  %{buildroot}%{_mandir}/man1/beet.1
install -Dm0644 docs/_build/man/beetsconfig.5 \
  %{buildroot}%{_mandir}/man5/beetsconfig.5
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a docs/_build/html %{buildroot}%{_docdir}/%{name}/html
rm -f %{buildroot}%{_docdir}/%{name}/html/.buildinfo
%oreon_autofiles beets-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files
%files -n beets-doc -f %{oreon_filedir}/beets-doc.list

%changelog

%autochangelog
