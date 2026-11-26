Scope and proposed review sequence
=======================================

Requested decisions
-------------------

For Theme 16 / UC-4, review the bounded source facts and expected observations
in FP-DC-001 before an implementation mapping is prepared. The case retains
Matrix v0.2 and D1 v0.1 as the discussion's existing baseline; it does not
propose editing either. A source-review freeze and any experimental integration
remain separate decisions by the interested contributors.

For PR 15, review the separate, attributed authority-provenance mapping as
informative input to that charter's D2. Its selected FP records and declared
hypothetical regime make the carriage questions inspectable. The draft does not
propose charter wording or a completed assessment against unpublished or
unexamined decision tables.

For the proposed WG2 evaluation fixtures, consider whether FP-DC-001 fits an
existing fixture work item after source review. Request an allocation, rather
than assuming that publication creates a work item or a meeting presentation.

What the Foundation Protocol reference contributes
-------------------------------------------------------

The source covers persistent entities, governed relationships, owner escalation,
contract coordination and accounting, and verifiable records. This contribution
uses that broader architecture to separate the following interfaces:

.. list-table:: Research reference and discussion boundary
   :header-rows: 1

   * - FP reference surface
     - Question for the existing discussion
     - Initial evidence
   * - Owner escalation and pending actions
     - Theme 16: what state did the reviewer decide on?
     - C0-C2 and the presented-state record
   * - Relationship and contract-role gates
     - WG2: what permits the particular action at the current boundary?
     - Separate grant, policy and review inputs
   * - Signed envelopes and contract snapshots
     - Theme 5 / D2: what authority facts can the selected record express?
     - Separate mapping with regime and attributed case stipulations
   * - Revocation and missing current status
     - Theme 60 / trust control plane: what was consulted and what follows?
     - C3-C4; explicit no-finding state when unreachable
   * - Acknowledgement and independently observed effect
     - Theme 13 / Theme 59: did the requested intervention take effect?
     - C5, without a measured propagation or kill-switch result

The v0.1 packet tests a single deferred execution boundary. It does not test
revocation fan-out, interruption of an already running operation, legal validity,
human understanding, or federated connection acceptance. Those require separate
source facts, controls and methods; they must not be inferred from these cases.
Institutional oversight capacity is unassessed, separately from the supplied
review authority and recorded response.

Version and evaluation policy
-----------------------------

The public Git commit is the citation boundary for this source proposal.
Publication fixes the cited bytes, but does not mean contributors have agreed
to freeze the reference semantics. Changes after review receive a new version.

An implementation assessment should pin its code, configuration and adapter;
report unsupported checks; retain independent expected outcomes; and publish
observed events separately. No runtime test, human study, timing measurement,
or paid model invocation is part of this v0.1 contribution.

References
----------

* `Source-packet request, 2 November <https://github.com/FG-TIDA/themes/issues/16#issuecomment-6579868295>`_
* `D2 invitation, 14 October <https://github.com/FG-TIDA/themes/pull/15#issuecomment-6180058259>`_
* `WG2 / control-plane interface v3 discussion <https://github.com/FG-TIDA/themes/issues/60#issuecomment-6920318845>`_
* `Proposed trust control plane <https://github.com/FG-TIDA/themes/issues/59>`_
* `Foundation Protocol paper v1 <https://arxiv.org/html/2605.23218v1>`_
