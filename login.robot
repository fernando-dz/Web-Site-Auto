*** Settings ***
Library     Browser
Resource    Web-Keys.robot
Documentation    Cross-browser login check against the Applitools ACME Bank demo
...              (https://demo.applitools.com) — Chromium, WebKit, and Firefox.
...
...              Originally included a "Bad Logins" test asserting an error message
...              appears for invalid credentials. Dropped 2026-09-25: verified live
...              against the real site that it has no credential validation anymore —
...              a blank or wrong login still reaches the dashboard, no error state
...              ever renders. Keeping a test that waits on an element the page never
...              shows doesn't verify anything; it just fails permanently for the
...              wrong reason.

*** Variables ***

*** Test Cases ***
Login To Acme
    Launch Acme Login   chromium
    Launch Acme Login   webkit
    Launch Acme Login   firefox
#Bad Logins
#    Launch Acme     chromium
#    AcmeBank Bad User
#    Launch Acme     webkit
#    Acmebank Bad User+Pass