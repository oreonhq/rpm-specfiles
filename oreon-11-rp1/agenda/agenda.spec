%global source0_hash 55e81dfd60a2fb85285a510d2cda1984b6a7d7bd15816c71e7326f0cd6bdb5bd
%global app_id com.github.dahenson.agenda
Name:           agenda
Summary:        A simple, slick, speedy and no-nonsense task manager
Version:        1.2.1
Release:        1%{?dist}
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND CC0-1.0
SourceLicense:  %{license} AND LGPL-2.0-or-later
URL:            https://github.com/dahenson/agenda
Source0:        https://github.com/dahenson/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
Requires:       hicolor-icon-theme
Summary(ca):    Un gestor de tasques fàcil d’utilitzar
Summary(de):    Ein einfacher, handlicher, schneller und nützlicher Aufgaben Verwalter
Summary(es):    Un administrador de tareas simple, pulido, rápido y sin complicaciones
Summary(fr):    Un gestionnaire de tâches simple, rapide et élégant
Summary(gl):    Un xestor de tarefas pulido, sinxelo, rápido e sen complicacións
Summary(it):    Un promemoria semplice, elegante, veloce e senza fronzoli
Summary(ja):    タスクを完了しましょう
Summary(ka):    მარტივი, მოხერხებული, სწრაფი დავალებების მმართველი ყოველგვარი უაზრობების გარეშე
Summary(ko):    간단하고 미려한 일정 관리자
Summary(lt):    Paprasta, vikri, greita, dalykiška užduočių tvarkytuvė
Summary(ms):    Pengurus tugas yang ringkas dan pantas
Summary(nl):    Rond taken af
Summary(pl):    Prosty, gładki, szybki i niebezsensowny menedżer zadań
Summary(pt):    Um gestor de tarefas simples, liso, rápido e sem falhas
Summary(ru):    Простой и быстрый менеджер задач
Summary(sr):    Једноставан, гладак, брз и без којештарија управник задатака
Summary(tr):    Basit, şık, hızlı ve zırvalıksız görev yöneticisi
Summary(ur):    ﺎﯿﮐ ﺱﺍﺩہ، ہﻮﺸﯾﺍﺭ، ﻑﻭﺮﯾ ﺍﻭﺭ ﺲﯾﺩﺍہ ﺱﺍﺩہ ٹﺎﺴﮐ ﻢﯿﻨﯿﺟﺭ
Summary(zh_CN): 简单流畅、快速不脑残的任务规划管理器
# oreon:deps
BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  hardlink
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  vala
# /oreon:deps
%description
A task manager to help you keep track of the tasks that matter most.

Sometimes, you just need a task list to keep you motivated. Agenda provides a
way to write down your tasks and tick them off as you complete them. The list
is saved automatically, so you can close the list to get it out of the way
without losing your place.

Key Features:

  • Saves your task list automatically
  • See your completed tasks until you choose to delete them
  • Autocompletion for previously added tasks
  • Undo/Redo with Ctrl-Z and Ctrl-Y
  • Quit with the Esc key

%description -l it
Un task manager per aiutarti a tenere traccia delle attività che contano di
più.

A volte, hai solo bisogno di un elenco di attività per mantenerti motivato.
Agenda fornisce un modo per annotare i tuoi compiti e spuntarli mentre li
completi. L'elenco viene salvato automaticamente, quindi puoi chiudere
l'elenco per estrarlo in modo senza perdere il tuo posto.

Caratteristiche principali:

  • Salva automaticamente l'elenco delle attività
  • Visualizza le tue attività completate finché non scegli di eliminarle
  • Completamento automatico per attività aggiunte in precedenza
  • Esci con il tasto Esc

%description -l ja
最も重要なタスクの記録に便利な、タスク管理アプリです。

モチベーションを維持するために、タスクリストが必要なときはありませんか。
Agenda を使えば、タスクを登録して、終わったらチェックマークをつけていくこと
ができます。リストは自動的に保存されるので、最新の状態を失うことなくリストを
閉じられます。

主な機能:

  • タスクリストを自動的に保存します
  • 完了したタスクは、削除しない限り確認できます
  • 以前に追加したタスクを自動補完します
  • Esc キーで終了できます

%description -l nl
Een taakbeheerder die u helpt de belangrijkste taken bij te houden.

Soms heeft u een taak nodig om u bezig te houden. Agenda biedt de mogelijkheid
uw taken te noteren en ze nadien af te vinken. De lijst wordt automatisch
opgeslagen, dus u kunt de lijst sluiten zonder uw taken kwijt te raken.

Kenmerken:

  • Slaat uw taken automatisch op
  • Bekijk uw afgeronde taken totdat u besluit ze te verwijderen
  • Taaknamen worden automatisch aangevuld
  • Sluit af met de Esc-toets

%description -l pt
Um gestor de tarefas que o ajuda a manter o controle das tarefas que são mais
importantes.

Às vezes, você só precisa precisa de uma lista de tarefas para o manter
motivado. O Agenda proporciona uma forma de escrever as suas tarefas e ir
assinalando aquelas que vai completando. A lista é gravada automaticamente,
para que a possa fechar e tira-la do seu caminho sem que se perca.

Funcionalidades principais:

  • Guarda a sua lista de tarefas automaticamente
  • Veja as suas tarefas completadas até decidir apaga-las
  • Preenchimento automático para tarefas adicionadas anteriormente
  • Fechar com a tecla Esc

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
%meson

%build

%meson_build
%install
%meson_install
%find_lang %{app_id}
hardlink -c -v '%{buildroot}%{_datadir}/icons/hicolor'
%oreon_autofiles main

%check

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{app_id}.appdata.xml
appstreamcli validate --no-net --explain \
    %{buildroot}/%{_metainfodir}/%{app_id}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
